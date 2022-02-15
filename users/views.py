from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from . forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required
from . models import Account
from django.core.paginator import Paginator

# ================
#   User Profile
# ================
@login_required(redirect_field_name='next',login_url='signin')
def userProfileView(request,username):
    account_owner = Account.objects.get(username=username)
    return render(request, 'userProfile.html', {'account_owner': account_owner})



# ================
#    Users List
# ================
@login_required(redirect_field_name='next',login_url='signin')
def userListView(request):
    users = Account.objects.all()
    page = request.GET.get('page', 1) # this set page to equal page 1
    paginator = Paginator(users, 4) # this breaks posts obj into groups of 4
    users = paginator.get_page(page) # this resets posts to equal paginator page 1
    return render(request, 'users_list.html', {'users':users})



# ============
#   Sign In
# ===========
def signinView(request):
    user =  request.user
    location = 'signin'
    if user.is_authenticated:
        return redirect('communityWall')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email,password=password)
            if user:
                login(request,user)
                return redirect('communityWall')
    else:
        form = AccountAuthenticationForm()
    return render(request, 'signin.html',{'form':form,'location':location})



# ============
#   Log Out
# ============
def signoutView(request):
    logout(request)
    return redirect('signin')



# =============
#  Create User
# =============
def registationView(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_user = form.save(commit=False)
            if request.POST.get('user_image'):
                new_user.user_image = request.FILES['user_image']
            new_user.save()
            email = form.cleaned_data.get('email')
            raw_pw = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_pw)
            login(request,account)
            return redirect('communityWall')
    else:
        form = RegistrationForm()
    return render(request, 'register.html',{'form':form})



# ===============
#   Update User
# ===============
@login_required(redirect_field_name='next',login_url='signin')
def userUpdateView(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = request.user
            if request.POST.get('user_image') == None:
                user.user_image = request.FILES['user_image']
            user.save()
            form.save()
        return redirect('communityWall')
    else:
        form = AccountUpdateForm(
            initial = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'username': request.user.username,
                'user_image': request.user.user_image,
                'bio': request.user.bio,
                'hobbies': request.user.hobbies,
                'favorite_tv': request.user.favorite_tv,
                'favorite_books': request.user.favorite_books,
                'work': request.user.work,
                'schools': request.user.schools,
            }
        )
    return render(request, 'user_update.html', {'form':form})

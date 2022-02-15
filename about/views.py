from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Blog, BlogLike
from . forms import BlogForm, BlogLikeForm
from users.models import Account
from django.core.paginator import Paginator

# Create your views here.

@login_required(redirect_field_name='next', login_url='signin')
def all_blogs_view(request):
    blogs = Blog.objects.all()
    users = Account.objects.all()

    page = request.GET.get('page', 1) # this set page to equal page 1
    paginator = Paginator(blogs, 4) # this breaks posts obj into groups of 4
    blogs = paginator.get_page(page) # this resets posts to equal paginator page 1

    if 'user_search' in request.POST:
        if request.POST.get('user_find') == 'search_user':
            user = request.POST.get('user')
            if str(user) == 'all':
                blogs = Blog.objects.all()
            else:
                blogs = []
                temp_blogs = Blog.objects.all()
                for blog in temp_blogs:
                    if str(blog.author) == str(user):
                        blogs.append(blog)

    if 'blog' in request.POST:
        if request.POST.get('create_blog') == 'blog':
            blog_form = BlogForm(data=request.POST)
            if blog_form.is_valid():
                new_blog = blog_form.save()
            return redirect('all_blogs')

    blog_form = BlogForm(initial={'author': request.user})
    context = {
        'blogs': blogs,
        'blog_form': blog_form,
        'users': users,
    }
    return render(request, 'blog.html', context)

@login_required(redirect_field_name='next', login_url='signin')
def single_blog_view(request, id):
    blog_id = Blog.objects.get(id=id)
    blog_likes = BlogLike.objects.filter(blog=id)

    does_user_like = False
    for bl in blog_likes:
        if str(bl) == str(request.user):
            does_user_like = True

    if request.POST:
        blog_like_form = BlogLikeForm(data=request.POST)
        if blog_like_form.is_valid():
            blog_like_form.save()
        blog_id.like += 1
        blog_id.save()
        return redirect(request.path_info)

    blog_like_form = BlogLikeForm(initial={'blog':id,'user': request.user})
    context = {
        'blog_id': blog_id,
        'blog_like_form': blog_like_form,
        'does_user_like': does_user_like,
    }
    return render(request, 'full_blog.html',context)

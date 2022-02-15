from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from . models import Account

# ==============
#    SIGN UP
# ==============
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=250, help_text="yourmail@domain.com")
    birth_date = forms.DateField(help_text="Please enter in YYYY-MM-DD format")

    class Meta:
        model = Account
        fields = ('first_name','last_name','email','username','birth_date','user_image','password1','password2')


# =============
#    SIGN IN
#  ============
class AccountAuthenticationForm(forms.ModelForm):
    password =  forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email','password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            print(email)
            print(password)
            if not authenticate(email=email,password=password):
                raise forms.ValidationError('Sorry, there was a login error.  Please verify email and password')


# =============
#  USER UPDATE
# =============
class AccountUpdateForm(forms.ModelForm):
    user_image = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = Account
        fields = ('first_name','last_name','email','username','user_image','bio','hobbies','favorite_tv','favorite_books','work','schools')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use' % email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use' % username)

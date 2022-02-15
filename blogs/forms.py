from django import forms
from . models import Blog, BlogLike
from django.forms import HiddenInput

class BlogForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(BlogForm, self).__init__(*args,**kwargs)
        self.fields['author'].widget = HiddenInput()

    class Meta:
        model = Blog
        fields = ('title','subject','content','author')

class BlogLikeForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(BlogLikeForm, self).__init__(*args,**kwargs)
        self.fields['blog'].widget = HiddenInput()
        self.fields['user'].widget = HiddenInput()

    class Meta:
        model = BlogLike
        fields = ('blog','user')

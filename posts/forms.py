from django import forms
from . models import Post, Comment, Reply, PostLike, CommentLike, ReplyLike
from django.forms import HiddenInput


# ============
#  Post Forms
# ============
class PostForm(forms.ModelForm):
    post_image = forms.ImageField(help_text="Please note, if you enter both a link and an image, the image will not show up.", required=False)
    # this function is to hide author input from user
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args,**kwargs)
        self.fields['link'].widget.attrs['placeholder'] = 'e.g http://www.legend-gary.com/'
        self.fields['author'].widget = HiddenInput()


    class Meta:
        model = Post
        fields = ('content','post_image','link','author')

# Post Like form
class PostLikeForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(PostLikeForm, self).__init__(*args,**kwargs)
        self.fields['post'].widget = HiddenInput()
        self.fields['user'].widget = HiddenInput()

    class Meta:
        model = PostLike
        fields = ('post','user')



# ===============
#  Comment Forms
# ===============
class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args,**kwargs)
        self.fields['author'].widget = HiddenInput()
        self.fields['post'].widget = HiddenInput()

    class Meta:
        model = Comment
        fields = ('content', 'author','post')

#  Comment Like Form
class CommentLikeForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(CommentLikeForm, self).__init__(*args,**kwargs)
        self.fields['comment'].widget = HiddenInput()
        self.fields['user'].widget = HiddenInput()

    class Meta:
        model = CommentLike
        fields = ('comment', 'user')


# ===============
#   Reply Forms
# ===============
class ReplyForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ReplyForm, self).__init__(*args,**kwargs)
        self.fields['author'].widget = HiddenInput()
        self.fields['comment'].widget = HiddenInput()

    class Meta:
        model = Reply
        fields = ('content', 'author', 'comment')

#   Reply Like Forms
class ReplyLikeForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ReplyLikeForm, self).__init__(*args,**kwargs)
        self.fields['reply'].widget = HiddenInput()
        self.fields['user'].widget = HiddenInput()

    class Meta:
        model = ReplyLike
        fields = ('reply', 'user')

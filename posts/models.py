from django.db import models

# ==========
#   Posts
# ==========
class Post(models.Model):
    content = models.TextField(max_length=1000)
    post_image = models.ImageField(verbose_name='post_picture', upload_to='post_img', null=True, blank=True)
    link = models.URLField(max_length=250, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('users.Account', on_delete=models.CASCADE)#users.Account is how to use modules from other app as ForeignKey
    like_count = models.IntegerField(default=0)

    class Meta:
        ordering = ('-create_date','author')
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return str(self.id)

#  Post Likes
class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey('users.Account', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.user)



# =============
#    Comments
# =============
class Comment(models.Model):
    content = models.CharField("", max_length=500)
    author = models.ForeignKey('users.Account', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)
    like_count = models.IntegerField(default=0)

    class Meta:
        ordering = ('create_date','author')
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return str(self.id)

#   Comment Likes
class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey('users.Account', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.user)



# ===========
#   Replies
# ===========
class Reply(models.Model):
    content = models.CharField("", max_length=500)
    author =  models.ForeignKey('users.Account', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)
    like_count = models.IntegerField(default=0)

    class Meta:
        ordering = ('create_date', 'author')
        verbose_name = 'reply'
        verbose_name_plural = 'replies'

    def __str__(self):
        return str(self.id)

#   Reply Likes
class ReplyLike(models.Model):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey('users.Account', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.user)

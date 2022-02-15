from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=75)
    subject = models.CharField(max_length=150)
    content = models.TextField(max_length=50000)
    author = models.ForeignKey('users.Account', on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)

    class Meta:
        ordering = ('-create_date', 'author', 'title')
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

    def __str__(self):
        return str(self.id)


class BlogLike(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey('users.Account', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

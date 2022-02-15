from django.contrib import admin
from . models import Post, Comment, Reply, PostLike, CommentLike, ReplyLike

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['create_date', 'author', 'content']
    list_per_page = 50
admin.site.register(Post,PostAdmin)

class PostLikeAdmin(admin.ModelAdmin):
    list_display = ['post','user']
    list_per_page = 50
admin.site.register(PostLike,PostLikeAdmin)





class CommentAdmin(admin.ModelAdmin):
    list_display = ['create_date', 'author', 'content']
    list_per_page = 50
admin.site.register(Comment,CommentAdmin)

class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ['comment', 'user']
    list_per_page = 50
admin.site.register(CommentLike, CommentLikeAdmin)





class ReplyAdmin(admin.ModelAdmin):
    list_display = ['create_date', 'author', 'content']
    list_per_page = 50
admin.site.register(Reply, ReplyAdmin)

class ReplyLikeAdmin(admin.ModelAdmin):
    list_display = ['reply', 'user']
    list_per_page = 50
admin.site.register(ReplyLike, ReplyLikeAdmin)

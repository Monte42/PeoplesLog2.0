from django.contrib import admin

from . models import Blog, BlogLike

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['create_date', 'author', 'title']
    list_per_page = 50
admin.site.register(Blog,BlogAdmin)

class BlogLikeAdmin(admin.ModelAdmin):
    list_display = ['blog', 'user']
    list_per_page = 50
admin.site.register(BlogLike,BlogLikeAdmin)

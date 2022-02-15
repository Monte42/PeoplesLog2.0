from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.all_blogs_view, name='all_blogs'),
    path('blogs/<id>/', views.single_blog_view),
]

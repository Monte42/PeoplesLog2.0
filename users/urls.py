from django.urls import path
from . import views

urlpatterns = [
    path('account/signin/', views.signinView, name='signin'),
    path('account/register/', views.registationView, name='register'),
    path('account/update/', views.userUpdateView, name='user_update'),
    path('account/logout/', views.signoutView, name='logout'),
    path('account/userList/', views.userListView, name='userList'),
    path('account/userProfile/<username>/', views.userProfileView, name='userProfile'),
]

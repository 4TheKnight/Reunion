from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.register,name="register"),
    path('update_profile/',views.profile,name='update_profile'),
    path('make_post/',views.make_post,name='makepost'),
    path('showpost/',views.show_post, name='post'),
    path('likepost/<int:post_id>',views.likepost, name='likepost'),
    path('comments/<int:post_id>',views.makecomment,name='makecomment'),
    path('showcomments/<int:post_id>',views.showcomments,name="showcomments"),
    path('likedby/<int:post_id>',views.liked_by,name="likedby"),
    path('userprofile/<str:profile_user>',views.view_profile,name="viewprofile"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('delete_user/',views.delete_user,name="delete_user"),
    path('deletepost/<int:post_id>',views.delete_post,name="deletepost"),
    path("",views.home,name="home")
]
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('signup', views.singup, name='signup'),
    path('login', views.userlogin, name='login'),
    path('logout', views.userlogout, name='logout'),
    path('create', views.create, name='create'),
    path('profile', views.profile, name='profile'),
    path('profileedit', views.profileedit, name='profileedit'),
    path('chat', views.chat, name='chat'),
    path('reset', views.custom_password_reset, name='resetpass'),
    # path('home', views.home, name='home'),
]
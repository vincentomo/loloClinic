from django.urls import path
from . import views

urlpatterns = [
    path('', views.accounts, name="home"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('about/', views.about, name='about'),
    path('profile/', views.userProfile, name='profile'),
    
]

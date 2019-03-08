from django.urls import path
from . import views

urlpatterns = [
    path('', views.accounts, name="home"),
    path('login/', accounts.user_login, name="login"),
    path('logout/', accounts.user_logout, name="logout")
    path('book/', views.book, name="book")
]
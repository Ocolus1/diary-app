from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('index/', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.loging_out, name="logout"),
]
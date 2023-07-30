from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

# app_name = AppName

urlpatterns = [
    # path('login/',views.user_login, name='login'),
    path("welcome",views.nameView,name="welcome"),
    path("logout",auth_views.LogoutView.as_view(),name="logout"), #this urls looks for templates in registration folder
    path("login",auth_views.LoginView.as_view(),name="login"),
    path('',views.dashboard,name="dashboard"),
]


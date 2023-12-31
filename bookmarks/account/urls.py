from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

# app_name = AppName

urlpatterns = [
    # path('login/',views.user_login, name='login'),
    path("welcome",views.nameView,name="welcome"),
    path("logout",auth_views.LogoutView.as_view(template_name="registration/logout.html"),name="logout"), #this urls looks for templates in registration folder
    path("login",auth_views.LoginView.as_view(),name="login"),
    path('',views.dashboard,name="dashboard"),
    # change Password urls
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    # reset password urls
    
    path('password_reset/',views.PasswordResetView.as_view(),name='password'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    # new user registration urls
    path('register/',views.register,name='register'),
    
    path('edit/',views.edit,name='edit')
]
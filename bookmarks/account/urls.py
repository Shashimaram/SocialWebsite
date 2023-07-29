from django.urls import path, re_path
from .views import user_login

# app_name = AppName

urlpatterns = [
    path('login/', user_login, name='login'),
]


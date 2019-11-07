# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

from django.conf.urls import url, include


urlpatterns = [
    # Login / Log Out
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='accounts/login.html'),
         name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(template_name='accounts/logout.html'),
         name='logout'),
      # Sign Up
     path('accounts/signup', views.sign_up, name="signup"), 
     url(r'^oauth/', include('social_django.urls', namespace='social')),  


]

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'
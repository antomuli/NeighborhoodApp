from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from . import views

app_name = 'api_auth'

urlpatterns = [
    path('signup', views.UserRegister.as_view(), name="signup"),
    path('login', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='refresh_token')
]
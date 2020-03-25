from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'api_auth'

urlpatterns = [
    path('signup', views.UserRegister.as_view()),
]
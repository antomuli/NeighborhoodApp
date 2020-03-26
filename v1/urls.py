from django.urls import path, include

from . import views

app_name = 'v1'

urlpatterns = [
    path('profile', views.ProfileDisplayView.as_view(), name="view_profile")
]
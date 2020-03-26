from django.urls import path, include

from . import views

app_name = 'v1'

urlpatterns = [
    path('profile', views.ProfileDisplayView.as_view(), name="view_profile"),
    path('hoods', views.HoodList.as_view(), name="list_hoods"),
    path('view_hood', views.HoodInfo.as_view(), name="view_hood"),
    path('create_hood', views.HoodCreateView.as_view(), name="create_hood"),
]
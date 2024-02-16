from django.urls import path
from . import views

urlpatterns = [
    path('', views.cms_home, name='cms_home'),
    path('add_user/', views.add_user, name='add_user'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('user_detail/', views.user_detail, name='user_detail'),
    path('add_door/', views.add_door, name='add_door'),
    path('door_detail/', views.door_detail, name='door_detail'),
    path('history/', views.history, name='history'),
    path('create_history/', views.create_history, name='create_history'),
]
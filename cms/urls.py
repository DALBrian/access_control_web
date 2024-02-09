from django.urls import path
from . import views

urlpatterns = [
    path('add_user/', views.add_user, name='add_user'),
    path('user_detail/', views.user_detail, name='user_detail'),
]
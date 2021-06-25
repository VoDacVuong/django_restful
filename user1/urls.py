from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('list_user/', views.listUser),
    path('user_detail/<str:key>/', views.DetailUser),
    path('create_user/', views.createUser),
    path('update_user/<str:key>/', views.update_user),
    path('delete_user/<str:key>/', views.delete_user),
]
    

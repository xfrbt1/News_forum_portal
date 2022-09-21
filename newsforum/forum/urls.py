from django.contrib import admin
from django.urls import path, include
from forum.views import post_detail
from forum import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('post_create/', views.post_create, name='post_create'),
    path('post_detail/<int:pk>', views.post_detail, name='post_detail'),




]

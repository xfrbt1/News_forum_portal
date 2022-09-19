from django.contrib import admin
from django.urls import path, include
from forum.views import PostCreateView, PostDetailView

from forum import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('<pk>/', PostDetailView.as_view(), name='post')



]

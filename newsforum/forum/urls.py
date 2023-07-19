from django.contrib import admin
from django.urls import path, include
# from forum.views import post_detail
from forum import views

urlpatterns = [
      path('', views.PostsView.as_view(), name='forum'),
      # path('post_detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
      path('post_create/', views.post_create, name='post_create'),
      # path('post_detail/<int:pk>', views.AddComment.as_view(), name='add_comment'),
      path('post_detail/<int:pk>', views.post_detail_view, name='post_detail'),

]



from django.contrib import admin
from django.urls import path, include

from forum import views

urlpatterns = [
    path('', views.forum, name='forum'),

]

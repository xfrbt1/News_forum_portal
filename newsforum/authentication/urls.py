from django.contrib import admin
from django.urls import path, include

from authentication import views

urlpatterns = [
    path('', views.login_page, name='auth_page'),
    path("registration/", views.reg_page, name='reg_page'),
    path('logout/', views.logout_user, name='logout')
]

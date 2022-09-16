from django.contrib import admin
from django.urls import path, include
from main.views import home, about
import authentication, news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    # path('authentication/', include('authentication.urls')),
    path('news/', include('news.urls')),
    path('forum/', include('forum.urls')),

]

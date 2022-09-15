from django.contrib import admin
from django.urls import path, include
from main.views import home
import authentication, news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # path('authentication/', include('authentication.urls')),
    # path('news/', include('news.urls')),

]

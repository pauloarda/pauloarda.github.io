from django.contrib import admin
from django.urls import path, include

from . views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('blog.urls')),
    path('users/', include('users.urls')),
    path('', index, name='index'),
]

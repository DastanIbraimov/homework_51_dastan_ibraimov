from django.contrib import admin
from django.urls import path

from webapp.views import index, show_info, update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('kitty/', show_info),
    path('update/', update)
]

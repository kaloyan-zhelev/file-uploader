from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('file_uploader.urls')),
    path('', include('contracts.urls')),
    path('admin/', admin.site.urls),
]

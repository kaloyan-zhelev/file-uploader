from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_upload, name='create_upload'),
    path('download-template', views.download_template, name='download_template'),
    path('apply-upload/<int:upload_id>', views.apply_upload, name='apply_upload'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_view, name='logout'),
]
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from . import views

app_name = 'fileupload'
urlpatterns = [
    url(r'^upload-file/', views.Upload.as_view(), name='upload'),
    url(r'^upload/$', TemplateView.as_view(template_name='upload.html'), name='upload-home'),

]
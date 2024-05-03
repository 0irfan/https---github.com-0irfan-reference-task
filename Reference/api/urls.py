from django.contrib import admin
from django.urls import path
from .views import FileUpload,FileDownload

urlpatterns = [
    
    path('file/', FileUpload.as_view()),
    path('file/<init:pk>',FileDownload.as_view(),)
]

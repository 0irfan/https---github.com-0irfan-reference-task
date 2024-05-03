from django.contrib import admin
from django.urls import path
from .views import Files,File,TaskList,TaskDetail

urlpatterns = [
    
    path('reference-file/', Files.as_view()),
    path('reference-file/<init:pk>',File.as_view()),
    path('task-list',TaskList.as_view()),
    path('task-detail',TaskDetail.as_view()),
]

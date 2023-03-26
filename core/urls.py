from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.StudentView.as_view(), name="studentpage"),
   
]
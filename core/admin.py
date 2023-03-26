from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['title','name','email','date']
  

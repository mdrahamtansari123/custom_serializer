from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    name = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=150)
    date = serializers.DateField()


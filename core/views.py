from django.shortcuts import render
from .models import Student
# Create your views here.
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework import status

class StudentView(APIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data  = request.data )
        
        if not serializer.is_valid():
            serializer.save()
            return Response({'status':403, 'errors': serializer.errors, 'message':'not post'})
        serializer.save()
        return Response({'status':200, 'payload': serializer.data, 'message':'succesfully'})
    
    # def create(self, validated_data):
    #     return Student.objects.create(**validated_data)
    
    def get(self, request, format=None):
        drinks = Student.objects.all()
        serializer = StudentSerializer(drinks, many=True)
        return Response(serializer.data)
    

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
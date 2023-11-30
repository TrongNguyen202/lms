# authentication_app/serializers.py
from rest_framework import serializers
from .models import CustomUser, Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description']

class CustomUserSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = CustomUser
        fields = [ 'username', 'email', 'verification_code', 'password', 'avatar_url']

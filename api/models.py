# authentication_app/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission



class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True)

    verification_code = models.CharField(max_length=6, blank=True, null=True)
    avatar_url = models.URLField(blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    courses = models.ManyToManyField('Course', related_name='users', blank=True)
    
    
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from .models import Task
from .serializers import UserSerializer, TaskSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    pass
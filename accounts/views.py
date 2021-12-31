from django.shortcuts import render
from rest_framework import viewsets , permissions
from .models import MyUser as User
from .serializers import MyUserSerializer

# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [permissions.IsAdminUser]
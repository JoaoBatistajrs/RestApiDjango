from django.shortcuts import render
from rest_framework import viewsets
from financepy.models import Register
from config.serializer import RegisterSerializer

class RegisterViewSet(viewsets.ModelViewSet):
  queryset = Register.objects.all()
  serializer_class = RegisterSerializer
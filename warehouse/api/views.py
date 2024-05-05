from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Seed
from .serializers import SeedSerializer
from django.views import generic
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
class SeedCreate(generics.CreateAPIView):
    queryset = Seed.objects.all()
    serializer_class = SeedSerializer
    

class SeedListCreate(generics.ListCreateAPIView):
    queryset = Seed.objects.all()
    serializer_class = SeedSerializer
    
    def post(self, *args, **kwargs):
        super().post(*args, **kwargs)
        return redirect('api:all')
    

class SeedRetrieve(generics.RetrieveAPIView):
    queryset = Seed.objects.all()
    serializer_class = SeedSerializer

    
class SeedRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seed.objects.all()
    serializer_class = SeedSerializer
    lookup_field = "pk"


class SeedDetroy(generics.RetrieveDestroyAPIView):
    queryset = Seed.objects.all()
    serializer_class = SeedSerializer
    lookup_field = "pk"

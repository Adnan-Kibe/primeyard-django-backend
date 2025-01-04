from django.shortcuts import render
from rest_framework import generics
from .models import Property, Inquiries
from .permissions import IsOwner
from .serializers import PropertySerializer, InquireSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# Create your views here.
class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.prefetch_related('images').all()
    serializer_class = PropertySerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        if self.request.method in ['POST']:
            return [IsAuthenticated()]
        return super().get_permissions()

class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.prefetch_related('images').all()
    serializer_class = PropertySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), IsOwner()]
        return super().get_permissions()

class InquireAPIView(generics.CreateAPIView):
    queryset = Inquiries.objects.all()
    serializer_class = InquireSerializer

class InquireDetailView(generics.RetrieveDestroyAPIView):
    queryset = Inquiries.objects.all()
    serializer_class = InquireSerializer
    permission_classes = [IsAuthenticated]

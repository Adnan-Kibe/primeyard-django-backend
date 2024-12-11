from rest_framework import serializers
from .models import Property, Image, Inquires
from main.serializers import UserSerializer

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("image_id", "image",)

class InquireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquires
        fields = ("inquire_id", "property", "name", "email", "phone", "message")

class PropertySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    inquiries = InquireSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = ("property_id", "user", "name", "address", "description", "price", "bedrooms", "bathrooms", "square_feet", "latitude","longitude", "status", "images","inquiries", "is_featured")
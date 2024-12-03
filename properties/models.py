import uuid
from django.db import models
from main.models import User

# Create your models here.
class StatusChoices(models.TextChoices):
    FOR_SALE = 'For Sale'
    FOR_RENT = 'For Rent'
    SOLD = 'Sold'

class Image(models.Model):
    image_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    property = models.ForeignKey('Property', on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return self.image.name


class Property(models.Model):
    property_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    square_feet = models.IntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default='FOR_SALE')
    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.address}"
    
class Inquires(models.Model):
    inquire_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="inquiries")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
    

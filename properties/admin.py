from django.contrib import admin
from .models import Property, Image, Inquires

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class InquiresInline(admin.StackedInline):
    model = Inquires

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ImageInline, InquiresInline] 

# Register your models here.
admin.site.register(Property, PropertyAdmin)
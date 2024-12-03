from django.urls import path
from . import views

urlpatterns = [
    path("", views.PropertyListCreateView.as_view(), name="property-list-create"),
    path("<uuid:pk>/", views.PropertyDetailView.as_view(), name="property-detail"),
    path("<uuid:pk>/inquire/", views.InquireAPIView.as_view(), name="inquire"),
    path("inquires/<uuid:pk>/", views.InquireDetailView.as_view(), name="inquire-detail"),
]

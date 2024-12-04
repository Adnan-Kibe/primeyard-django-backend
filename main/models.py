from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password
from datetime import timedelta
from django.utils.timezone import now

class User(AbstractUser):
    # class UserChoices(models.TextChoices):
    #     ADMIN = "ADMIN"
    #     AGENT = "AGENT"

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, null=True, blank=True) 
    # role = models.CharField(max_length=10, choices=UserChoices.choices, default=UserChoices.AGENT)
    # managed_agents = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="agents")
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    # Use email as the unique identifier
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Exclude username from required fields

    def __str__(self):
        return f"{self.username}"

    class Meta:
        db_table = "primeyard_user"

# class OTP(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     otp_hash = models.CharField(max_length=128)
#     created_at = models.DateTimeField(auto_now_add=True)
#     expires_at = models.DateTimeField(default=lambda: now() + timedelta(minutes=5))

#     def set_otp(self, otp):
#         """
#         Hashes and stores the OTP.
#         """
#         self.otp_hash = make_password(otp)

#     def verify_otp(self, otp):
#         """
#         Verifies if the given OTP matches the hashed OTP.
#         """
#         if self.is_valid() and check_password(otp, self.otp_hash):
#             return True
#         return False

#     def is_valid(self):
#         """
#         Checks if the OTP is still valid (not expired).
#         """
#         return now() <= self.expires_at

#     def __str__(self):
#         return f"OTP for {self.user.email}"
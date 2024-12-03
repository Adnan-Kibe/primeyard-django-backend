from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

class User(AbstractUser):
    class UserChoices(models.TextChoices):
        ADMIN = "ADMIN"
        AGENT = "AGENT"

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, null=True, blank=True) 
    role = models.CharField(max_length=10, choices=UserChoices.choices, default=UserChoices.AGENT)
    managed_agents = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="agents")
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    # Use email as the unique identifier
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Exclude username from required fields

    def __str__(self):
        return f"{self.email} - {self.get_role_display()}"

    class Meta:
        db_table = "primeyard_user"

# class OTP(models.Model):
#     class OTPType(models.TextChoices):
#         REGISTRATION = "REGISTRATION", "Registration"
#         PASSWORD_RESET = "PASSWORD_RESET", "Password Reset"

#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="otps")
#     otp = models.CharField(max_length=6)
#     otp_type = models.CharField(max_length=20, choices=OTPType.choices)
#     created_at = models.DateTimeField(auto_now_add=True)
#     expires_at = models.DateTimeField()

#     def is_valid(self):
#         return now() <= self.expires_at

#     def __str__(self):
#         return f"OTP({self.otp}) for {self.user.email} - {self.otp_type}"
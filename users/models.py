from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUSer(AbstractUser):
    is_admin = models.BooleanField(default=False)

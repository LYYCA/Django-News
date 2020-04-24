from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    # null is database related: when a field has null=True, it can store a 
    # database entry as NULL
    # blank is validation related: if blank=True, then a form will allow
    # an empty value, whereas if blank=False, then a value is required
    age = models.PositiveIntegerField(null=True, blank=True)


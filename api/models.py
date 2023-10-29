from django.db import models
from django.contrib.auth.models import User


class Staff(models.Model):
    staff = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='staff')

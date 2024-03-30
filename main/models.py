from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Survey_filled(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False) 
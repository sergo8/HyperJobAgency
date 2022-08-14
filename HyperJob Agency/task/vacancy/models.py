from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Vacancy(models.Model):
    description = models.CharField(max_length=1024)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
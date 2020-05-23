from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
class MyUser(AbstractUser):
    display_name = models.CharField(max_length=50, null=True, blank=True)
    #age = models.IntegerField()

    def __str__(self):
        return self.display_name
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models




class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True),
    education = models.CharField(max_length=100, verbose_name='Введите образование')


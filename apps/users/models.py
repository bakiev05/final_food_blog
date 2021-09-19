from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (
        ('m', 'Men'),
        ('f', 'Female'),
        ("Another", 'another'),
    )
    username = models.CharField(
        max_length=255,
        unique=True
    )
    profile = models.ImageField(
        upload_to='profiles',
        blank=True, null=True
    )
    bio = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    age = models.PositiveIntegerField(
        default=0
    )
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=255
    )

    def __str__(self):
        return f"{self.username}--{self.gender} "


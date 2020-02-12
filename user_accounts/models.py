from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional fields go here
    profile_photo = models.ImageField(upload_to='profile_photos', blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

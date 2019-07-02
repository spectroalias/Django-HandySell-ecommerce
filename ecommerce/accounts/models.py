from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
# class Usermodel(models.Model,User):
#     def get_absolute_url(self):
#             return reverse('user_detail')

class GuestUser(models.Model):
    email       =models.EmailField(null=False)
    timestamp   =models.DateTimeField( auto_now_add=True)
    update      =models.DateTimeField(auto_now=True)
    active      =models.BooleanField(default=True)

    def __str__(self):
        return self.email
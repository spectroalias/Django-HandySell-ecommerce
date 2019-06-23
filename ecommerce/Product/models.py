from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model,get_user
from django.utils.timezone import now
from django.db.models.signals import m2m_changed


class Product(models.Model):
    seller      = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,default=User)
    title       = models.CharField(max_length=150)
    description = models.TextField(null=True)
    price       = models.PositiveSmallIntegerField()
    image       = models.URLField(max_length=150)
    arrival_date= models.DateTimeField(default=now())
    # representation
    def comments(self):
        return self.comments.all()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("home")


class Comment(models.Model):
    product     =models.ForeignKey('Product.product',related_name='comments',on_delete=models.CASCADE)
    author      =models.CharField(default=User.username, max_length=150)
    text        =models.TextField(max_length=200)
    created_date=models.DateTimeField(default=now())

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("product_detail")
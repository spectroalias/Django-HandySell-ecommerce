from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model,get_user
from django.utils.timezone import now
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator

class Product(models.Model):
    seller      = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,default=User)
    slug        = models.SlugField(blank=True, unique=True)
    title       = models.CharField(max_length=150)
    description = models.TextField(null=True)
    price       = models.PositiveSmallIntegerField()
    image       = models.URLField(max_length=150)
    arrival_date= models.DateTimeField(auto_now=True)
    # representation

# slug is not in use yet

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("products:product_detail")

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.

class BillingProfile(models.Model):
    user        =models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    email       =models.EmailField(unique=True, max_length=254)
    timestamp   =models.DateTimeField( auto_now_add=True)
    update      =models.DateTimeField(auto_now=True)
    active      =models.BooleanField(default=True)

    def __str__(self):
        return self.email

def user_bill_profile_creation_reciever(sender,instance,created,*args,**kwargs):
    if created:
        BillingProfile.objects.get_or_create(user=instance,email=instance.email)

post_save.connect(user_bill_profile_creation_reciever,sender=User)

# reciever function for request for payment portal profile
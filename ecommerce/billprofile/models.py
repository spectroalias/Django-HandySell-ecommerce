from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from accounts.models import GuestUser
# Create your models here.

User = get_user_model()

class BillingProfileManager(models.Manager):
    def new_or_get(self,request):
        user = request.user
        gemail=request.session.get('guest_email_id')
        bill_profile=None
        new_bill = False
        if user.is_authenticated:
            bill_profile,new_bill=BillingProfile.objects.get_or_create(user=user,email=user.email)
        elif gemail is not None:
            guest=GuestUser.objects.filter(id=gemail)
            if guest.count() >=1 :
                guest = guest.first()
                bill_profile,new_bill=BillingProfile.objects.get_or_create(email=guest.email)
            else:
                del request.session['guest_email_id']
        else:
            print("Error in making bill profile")
        return bill_profile,new_bill


class BillingProfile(models.Model):
    user        =models.OneToOneField(User,null=True,blank=True,on_delete= models.SET_NULL)
    email       =models.EmailField(unique=True, max_length=254)
    timestamp   =models.DateTimeField( auto_now_add=True)
    update      =models.DateTimeField(auto_now=True)
    active      =models.BooleanField(default=True)

    objects = BillingProfileManager()
    def __str__(self):
        return self.email

def user_bill_profile_creation_reciever(sender,instance,created,*args,**kwargs):
    if created:
        BillingProfile.objects.get_or_create(user=instance,email=instance.email)

post_save.connect(user_bill_profile_creation_reciever,sender=User)

# reciever function for request for payment portal profile
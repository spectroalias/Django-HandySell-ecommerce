from django.db import models
from billprofile.models import BillingProfile
# Create your models here.


def getcountry_choices():
    countries = (('india','India'),('uk','UK'))
    return countries

class Address(models.Model):
    billing_profle  = models.ForeignKey(BillingProfile,on_delete= models.CASCADE, related_name="bill_profile") 
    address_type    = models.CharField(max_length=120,choices=(('billing','Billing'),('shipping','Shipping')))
    add_line_1      = models.CharField(max_length=120)
    add_line_2      = models.CharField(max_length=120)
    city            = models.CharField(max_length=120)
    pincode         = models.PositiveIntegerField(max_length=120)
    country         = models.CharField(max_length=120,choices=getcountry_choices())

    def __str__(self):
        return str(self.billing_profle)
from django.db import models
from django.db.models.signals import post_save,pre_save
from .utils import order_id_generator
from cart.models import Cart
# Create your models here.

Order_Status=(
    ('created','Created'),
    ('shipped','Shipped'),
    ('delivered','Delivered'),
    ('refunded','Refunded')
)


class Order(models.Model):
    order_id        =models.CharField(max_length=50,blank=True)
    # billing profle
    # ship add
    # bill add
    cart            =models.ForeignKey(Cart,on_delete=models.CASCADE)
    status          =models.CharField(default='created',choices=Order_Status, max_length=50)
    shipping_total  =models.DecimalField(default=20.50, max_digits=5, decimal_places=2)
    total           =models.DecimalField(max_digits=7, decimal_places=2,default=0.0)

    def __str__(self):
        return self.order_id
    
    def total_updation(self):
        self.total=float(self.cart.total)+float(self.shipping_total)
        self.save()

def pre_save_reciever_id_gen(sender,instance,*args,**kwargs):
    if not instance.order_id:
        instance.order_id=order_id_generator(instance).upper()

        
pre_save.connect(pre_save_reciever_id_gen,sender=Order)

# REDUCING CODE REDUNDANT RUNNING

# if order total changes due to updation of cart
def post_save_reciever_total_cart(sender,instance,created,*args,**kwargs):
    if not created:
        qs=Order.objects.filter(cart__id=instance.id) #cart(in order model)->id=instance(cart)->id
        if qs.count()==1:
            qs.first().total_updation()

post_save.connect(post_save_reciever_total_cart,sender=Cart)

# if order is just created 
def post_save_recieve_order(instance,sender,created,*args, **kwargs):
    if created:
        instance.total_updation()

post_save.connect(post_save_recieve_order,sender=Order)
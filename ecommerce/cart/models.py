from django.db import models
from django.contrib.auth import get_user_model
from Product.models import Product
from django.db.models.signals import m2m_changed,pre_save
# Create your models here.

User = get_user_model()

class CartModel_Manager(models.Manager):
    def new_cart(self,user=None):
        user_obj=None
        if user is not None:
            if user.is_authenticated:
                user_obj=user
        return self.model.objects.create(user=user_obj)

    def new_or_get(self,request):
        cart_id=request.session.get('cart_id',None)
        c=self.get_queryset().filter(id=cart_id)
        if c.count()==1:
            new_obj=False
            cart_obj=c.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user=request.user
                cart_obj.save()
        else:
            new_obj=True
            cart_obj=Cart.objects.new_cart(user=request.user)
            request.session['cart_id']=cart_obj.id
        return cart_obj,new_obj



class Cart(models.Model):
    user        =models.ForeignKey(User,null=True,blank=True,on_delete= models.SET_NULL)
    products    =models.ManyToManyField(Product,blank=True)
    total       =models.DecimalField(default=0.0,max_digits=7, decimal_places=2)
    sub_total   =models.DecimalField(default=0.0,max_digits=7, decimal_places=2)
    timestamp   =models.DateTimeField( auto_now=False, auto_now_add=True)
    updated     =models.DateTimeField( auto_now=True, auto_now_add=False)
    
    objects     =CartModel_Manager()

    def __str__(self):
        return str(self.id)



def total_change_action_reciever(sender,instance,action,*args, **kwargs):
    # print(action)
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products=instance.products.all()
        total=0.0
        for x in products:
            total+=x.price
        if total != instance.sub_total:
            instance.sub_total=total
            instance.save()

m2m_changed.connect(total_change_action_reciever, sender=Cart.products.through)



def additional_actions_cart_reciever(sender,instance,*args,**kwargs):
    if instance.sub_total > 0:
        instance.total=20+instance.sub_total #delivery charge and taxes
    else:
        instance.total=0.0 
        
pre_save.connect(additional_actions_cart_reciever,sender=Cart)
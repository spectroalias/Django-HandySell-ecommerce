from django.shortcuts import render,redirect
from cart.models import Cart
from cart.views import cart_home
from .models import Order
from accounts.forms import UserLoginForm,GuestForm
from billprofile.models import BillingProfile
from accounts.models import GuestUser
# Create your views here.

def order_checkout(request):
    cart_obj,new=Cart.objects.new_or_get(request)
    obj=None
    if new or cart_obj.products.count()==0:
        return redirect('cart:home')
    else:
        obj,new_order=Order.objects.get_or_create(cart=cart_obj,billing_profle=None)
    user=request.user
    login_form=UserLoginForm()
    guest_user_form=GuestForm()
    gemail=request.session.get('guest_email_id')
    bill_profile=None
    if user.is_authenticated:
        bill_profile,new_bill=BillingProfile.objects.get_or_create(user=user,email=user.email)
    elif gemail is not None:
        bill_profile,new_guest_bill=BillingProfile.objects.get_or_create(email=gemail)
        guest=GuestUser.objects.get(id=gemail)
    else:
        pass
    
    return render(request,'order/checkout.html',{'order':obj,'bill_profile':bill_profile,'form':login_form,'guest_form':guest_user_form})
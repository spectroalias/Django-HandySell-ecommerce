from django.shortcuts import render,redirect
from cart.models import Cart
from cart.views import cart_home
from .models import Order
from accounts.forms import UserLoginForm,GuestForm
from addresses.forms import AddressForm
from addresses.models import Address
from billprofile.models import BillingProfile
from accounts.models import GuestUser
from addresses.models import Address
# Create your views here.

def order_checkout(request):
    cart_obj,new=Cart.objects.new_or_get(request)
    if new or cart_obj.products.count()==0:
        return redirect('cart:home')
    login_form=UserLoginForm()
    guest_user_form=GuestForm()
    ship_add_form=AddressForm()
    bill_add_form=AddressForm()
    
    billing_address_id = request.session.get("billing_address_id", None)
    shipping_address_id = request.session.get("shipping_address_id", None)
    bill_profile,created = BillingProfile.objects.new_or_get(request)
    order_obj = None
    address_qs = Address.objects.filter(billing_profle=bill_profile)

    if bill_profile is not None:
        # if there are other objects then make them inactive for now,
        if request.user.is_authenticated:
            address_qs = Address.objects.filter(billing_profle=bill_profile)
        order_qs = Order.objects.filter(billing_profle=bill_profile, cart=cart_obj,active=True,status="created")
        if order_qs.count()>=1:
            order_obj=order_qs.first()
        else:
            order_obj= Order.objects.create(cart=cart_obj,billing_profle=bill_profile)
        if billing_address_id:
            order_obj.bill_add=Address.objects.get(id=billing_address_id)
            del request.session["billing_address_id"]
        if shipping_address_id:
            order_obj.ship_add=Address.objects.get(id=shipping_address_id)
            del request.session["shipping_address_id"]
        if billing_address_id or shipping_address_id:
            order_obj.save()
    if request.method == 'POST':
        isvalid = order_obj.final_check()
        if isvalid:
            order_obj.status_paid()
            del request.session["cart_id"]
            request.session["cart_items"] = 0
            return render(request,"order/success.html",{})
    responseData = {
        'ship_add':ship_add_form,
        'bill_add':bill_add_form,
        'order':order_obj,
        'bill_profile':bill_profile,
        'form':login_form,
        'guest_form':guest_user_form,
        'address_qs':address_qs
    }
    return render(request,'order/checkout.html',responseData)

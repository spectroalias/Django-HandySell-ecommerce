from django.shortcuts import render,redirect
from .models import Cart
from Product.models import Product 
from order.models import Order
from django.utils.http import is_safe_url 
# Create your views here.

def cart_home(request):
    cart,new=Cart.objects.new_or_get(request)
    request.session['cart_items']=cart.products.all().count()
    return render(request,'cart/cart_view.html',{'cart':cart})

def cart_update(request):
    product_id=request.POST.get('product_id')
    _next = request.POST.get('next')[0:-1]
    q = request.POST.get('q',None)
    if q:
        _next+=('?q='+q[0:-1])
    if product_id is not None:
        try:
            product_obj=Product.objects.get(id=product_id)
        except Product.DoesNotExixt:
            print("something is wrong")
            return redirect(_next)
        cart,new=Cart.objects.new_or_get(request)
        if product_obj in cart.products.all():
            cart.products.remove(product_obj)
            request.session['cart_items']=cart.products.all().count()
        else:
            cart.products.add(product_obj)
            request.session['cart_items']=cart.products.all().count()
    return redirect(_next)

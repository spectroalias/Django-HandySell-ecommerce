from django.shortcuts import render,redirect
from .models import Cart
from Product.models import Product 
from order.models import Order
from django.utils.http import is_safe_url 
from django.http import JsonResponse
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
        productAdded = False
        try:
            product_obj=Product.objects.get(id=product_id)
        except Product.DoesNotExixt:
            print("something is wrong")
            return redirect(_next)
        cart,new=Cart.objects.new_or_get(request)
        if product_obj in cart.products.all():
            cart.products.remove(product_obj)
        else:
            cart.products.add(product_obj)
            productAdded = True
        cart_count = cart.products.all().count()
        request.session['cart_items']=cart_count
        if request.is_ajax(): #if ajax call is made then what should be the response
            jsonData = {
                "added":productAdded,
                "removed": not productAdded,
                "cart_count":cart_count,
                "cart_total":cart.sub_total,
                "total_amount":cart.total,
            }
            return JsonResponse(jsonData)
    return redirect(_next)

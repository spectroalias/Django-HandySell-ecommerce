from django.shortcuts import render,redirect
from .models import Cart
from Product.models import Product 
# Create your views here.

def cart_home(request):
    cart,new=Cart.objects.new_or_get(request)
    return render(request,'cart/cart_view.html',{'cart':cart})

def cart_update(request):
    product_id=request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj=Product.objects.get(id=product_id)
        except Product.DoesNotExixt:
            print("something is wrong")
            return redirect("cart:home")
        cart,new=Cart.objects.new_or_get(request)
        if product_obj in cart.products.all():
            cart.products.remove(product_obj)
        else:
            cart.products.add(product_obj)
    return redirect("cart:home")
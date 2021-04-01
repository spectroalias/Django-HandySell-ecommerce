from django.shortcuts import render,redirect
from .models import Address
from .forms import AddressForm
from billprofile.models import BillingProfile
from django.utils.http import is_safe_url 

# Create your views here.

def checkout_address_create(request):
    form=AddressForm(request.POST or None)
    next_=request.GET.get('next')
    next_post=request.POST.get('next')
    redirect_urls=next_ or next_post or None
    if form.is_valid():
        instance = form.save(commit=False)
        billing_profle, iscreated = BillingProfile.objects.new_or_get(request)
        if billing_profle is not None:
            instance.billing_profle = billing_profle
            address_type = request.POST.get('address_type','shipping')
            # instance.address_type = address_type
            instance.save() 
            request.session[address_type+"_address_id"] = instance.id
            if request.POST.get('same_bill_add') and address_type == 'shipping':
                add_obj= Address.objects.get(pk=instance.id)
                if add_obj:
                    # add_obj.pk=None
                    # # add_obj.address_type='billing'
                    # add_obj.save()
                    request.session["billing_address_id"] = add_obj.id
                else:
                    print("some happen with the add save .... re-enter of address required")
        else :
            return redirect('order:checkout')
        if is_safe_url(redirect_urls,request.get_host()):
            return redirect(redirect_urls)
        else:
            return redirect('order:checkout')
    return redirect('order:checkout')


def checkout_address_reuse(request):
    form=AddressForm(request.POST or None)
    next_=request.GET.get('next')
    next_post=request.POST.get('next')
    redirect_urls=next_ or next_post or None
    if request.method == 'POST':
        address_id = request.POST.get("address_id")
        billing_profle, iscreated = BillingProfile.objects.new_or_get(request)
        if billing_profle is not None:
            address_type = request.POST.get('address_type','shipping')
            add_obj = Address.objects.filter(id=address_id,billing_profle=billing_profle)
            if add_obj.count()>0 :
                add_obj=add_obj.first()
                # add_obj.address_type = address_type
                request.session[address_type+"_address_id"] = add_obj.id
            else :
                print("Something went wrong...on address side.")
            return redirect('order:checkout')
        if is_safe_url(redirect_urls,request.get_host()):
            return redirect(redirect_urls)
        else:
            return redirect('order:checkout')
    return redirect('order:checkout')
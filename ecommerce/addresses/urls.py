from django.urls import path,include
from django.conf.urls import url
from .views import checkout_address_create, checkout_address_reuse
app_name = 'address'

urlpatterns = [
    url(r'^address/reuse$',checkout_address_reuse,name="checkout_address_reuse"),
    url(r'^address/create$',checkout_address_create,name="checkout_address_create"),

]

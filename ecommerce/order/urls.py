from django.urls import path,include
from .views import order_checkout,GeneratePdf
app_name='order'

urlpatterns = [
    path("checkout",order_checkout,name="checkout"),
    path("success",order_checkout,name="success"),
    path("saveAs/?P<order_id>",GeneratePdf.as_view(),name="save_as_pdf"),

]
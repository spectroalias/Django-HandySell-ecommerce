from django.urls import path,include
from .views import order_checkout,GeneratePdf,my_orders, order_detailView
app_name='order'

urlpatterns = [
    path("checkout",order_checkout,name="checkout"),
    path("success",order_checkout,name="success"),
    path("invoice/?P<order_id>",order_detailView,name="invoice"),
    path("saveAs/?P<order_id>",GeneratePdf.as_view(),name="save_as_pdf"),
    path("myOrders/",my_orders,name="my_orders"),

]
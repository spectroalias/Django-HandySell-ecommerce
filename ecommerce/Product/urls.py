from .views import ProductListView ,ProductDetailView,DeleteProductView,UpdateProductView,add_product, myProductsListView 
from django.urls import path
app_name = 'product'

urlpatterns=[
    path('home/',ProductListView.as_view(), name="home"),
    path(r'?P<slug>/',ProductDetailView.as_view(),name="product_detail"),
    path(r'delete/?P<slug>/',DeleteProductView.as_view(),name="product_delete"),
    path(r'update/product/?P<slug>/',UpdateProductView,name="product_update"),
    path(r'product_add/',add_product,name='add_product'),
    path(r'myProduct/',myProductsListView,name="my_products"),

]
from .views import ProductListView ,ProductDetailView,DeleteProductView,UpdateProductView,add_product, myProductsListView 
from django.urls import path
app_name = 'product'

urlpatterns=[
    path('home/',ProductListView.as_view(), name="home"),
    path('product/<int:pk>/',ProductDetailView.as_view(),name="product_detail"),
    path('product/delete/<int:pk>/',DeleteProductView.as_view(),name="product_delete"),
    path('update/product/<int:pk>/',UpdateProductView,name="product_update"),
    path('product_add/',add_product,name='add_product'),
    path('myProduct/',myProductsListView,name="my_products"),

]
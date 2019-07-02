"""ecomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from accounts.views import index,about_us,contact_us,LogoutView,LoginView, RegisterView,UpdateUserView,UserDetailView,DeleteUserView,change_password,GuestView
from django.conf import settings
from django.conf.urls.static import static
from Product.views import ProductListView ,ProductDetailView,comment_detail,DeleteProductView,UpdateProductView,add_comment, comment_remove,add_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',ProductListView.as_view(), name="home"),
    path('about_us/', about_us,name="about_us"),
    path('contact_us/', contact_us,name="contact_us"),
    path('login/guest/',GuestView,name="guest_login"),
    path('login/',LoginView,name="login"),
    path('register/',RegisterView,name="register"),
    path('logout/',LogoutView,name="logout"),
    path('product/<int:pk>/',ProductDetailView.as_view(),name="product_detail"),
    path('myself/<int:pk>/',UserDetailView.as_view(),name="user_detail"),
    path('user/delete/<int:pk>/',DeleteUserView.as_view(),name="user_delete"),
    path('product/delete/<int:pk>/',DeleteProductView.as_view(),name="product_delete"),
    # path('create/',CreateProductView.as_view(),name="product_create"),
    path('update/product/<int:pk>/',UpdateProductView.as_view(),name="product_update"),
    path('update/user/<int:pk>/',UpdateUserView.as_view(),name="user_update"),
    path('password/',change_password, name='change_password'),
    path('product/<int:pk>/comment/',add_comment,name='add_comment'),
    path('comment/<int:pk>/detail',comment_detail.as_view(),name='comment_detail'),
    path('comment/<int:pk>/delete',comment_remove,name='comment_delete'),
    path('search/', include('search.urls',namespace='search')),
    path('product_add/',add_product,name='add_product'),
    path('cart/', include('cart.urls',namespace='cart')),
    path('order/', include('order.urls',namespace='order')),


]

if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
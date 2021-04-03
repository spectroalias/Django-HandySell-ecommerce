from .views import about_us,LogoutView,LoginView, RegisterView,UpdateUserView,UserDetailView,DeleteUserView,change_password,GuestView
from django.urls import path ,include
app_name = 'account'

urlpatterns = [
    path('about_us/', about_us,name="about_us"),
    # path('contact_us/', contact_us,name="contact_us"),
    path('login/guest/',GuestView,name="guest_login"),
    path('login/',LoginView,name="login"),
    path('register/',RegisterView,name="register"),
    path('logout/',LogoutView,name="logout"),
    path('me/<int:pk>/',UserDetailView.as_view(),name="user_detail"),
    path('user/delete/<int:pk>/',DeleteUserView.as_view(),name="user_delete"),
    path('update_me/<int:pk>/',UpdateUserView.as_view(),name="user_update"),
    path('password/',change_password, name='change_password'),
]
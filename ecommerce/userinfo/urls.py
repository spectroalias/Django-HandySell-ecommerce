from django.urls import path
from .views import UpdateUserInfoView
app_name = 'userinfo'

urlpatterns = [
    path('edit/',UpdateUserInfoView ,name="edit_userinfo"),
]
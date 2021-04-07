from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import UserInfo
# Create your views here.

class UpdateUserInfoView(LoginRequiredMixin,UpdateView):
    model = UserInfo
    fields=['profile_pic','gender','contact']
    template_name='auth/userinfo_update.html'
    success_url=reverse_lazy('accounts:user_detail')
    def get_object(self):
        userinfo_obj,created =  UserInfo.objects.get_or_create(pk=self.request.user.userInfo.id)
        return userinfo_obj
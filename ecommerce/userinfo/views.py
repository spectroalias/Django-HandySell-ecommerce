from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect , render
from .models import UserInfo
from .forms import UserInfoForm
import os
# Create your views here.

@login_required
def UpdateUserInfoView(request):
    userInfo_obj = UserInfo.objects.get(id=request.user.userInfo.id)
    form = UserInfoForm(request.POST, request.FILES ,instance=userInfo_obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('accounts:user_detail')
    else:
        form = UserInfoForm(instance=userInfo_obj)
    data={
        'userInfo':userInfo_obj,
        'form':form,
    }
    return render(request,'auth/userinfo_update.html',context=data)

    
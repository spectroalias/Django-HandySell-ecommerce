from django import forms
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    model = UserInfo
    fields = ['profile_pic','gender','contact']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs['style']="width:100%;"
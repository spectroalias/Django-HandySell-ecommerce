from django import forms
from .models import UserInfo, genders

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('profile_pic','gender','contact')
        # widgets = {
        #     'profile_pic' : forms.ImageField(),
        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs['style']="width:20%;"
        self.fields['profile_pic'].widget.attrs['class']="form-control-file"
        
    
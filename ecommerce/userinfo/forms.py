from django import forms
from .models import UserInfo, genders

class UserInfoForm(forms.ModelForm):
    profile_pic = forms.ImageField(label=('Profile Avatar'),required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    class Meta:
        model = UserInfo
        fields = ('profile_pic','gender','contact')
        # widgets = {
        #     'profile_pic' : forms.ImageField(),
        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs['style']="width:100%;"
        self.fields['contact'].widget.attrs['style']="width:100%;"
        self.fields['profile_pic'].widget.attrs['class']="form-control-file"
        self.fields['profile_pic'].widget.attrs['style']="width:100%"
        
    
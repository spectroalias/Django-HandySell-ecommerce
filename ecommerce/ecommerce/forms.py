from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()
class UserLoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control" ,"placeholder":"Enter Your Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Your Password"}))
    
class UserRegisterForm(forms.Form):
    Username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control name" ,"placeholder":"Enter Your Username"}))
    Email=forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control mail","placeholder":"Type Your Email"}))
    Password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control pass","placeholder":"Enter Your Password"}))
    Confirm_password=forms.CharField(label="Confirm password",widget=forms.PasswordInput(attrs={"class":"form-control pass","placeholder":"Confirm Your Password"}))

    def clean_Username(self):
        uname=self.cleaned_data.get("Username")
        set=User.objects.filter(username=uname)
        if set.exists():
            raise forms.ValidationError("Username exist try another one.")
        return uname

    def clean_Email(self):
        email=self.cleaned_data.get("Email")
        set=User.objects.filter(email=email)
        if set.exists():
            raise forms.ValidationError("Email exist try another one.")
        return email

    def clean(self):
        data = self.cleaned_data
        Password = self.cleaned_data.get('Password')
        Password2 = self.cleaned_data.get('Confirm_password')
        if Password != Password2:
            raise forms.ValidationError("Passwords didn't match")
        return data
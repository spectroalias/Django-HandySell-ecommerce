from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from captcha.fields import CaptchaField,CaptchaTextInput

User=get_user_model()
class UserLoginForm(forms.Form):
    email=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control" ,"placeholder":"Enter Your Registered Email"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Your Password"}))
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'class':'form-control', "placeholder":"Enter the captcha", 'style':"margin-top:5px;margin-bottom:15px;"}))

class GuestForm(forms.Form):
    Email=forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control mail","placeholder":"Type Your Email",'required':'True'}))
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'class':'form-control', "placeholder":"Enter the captcha", 'style':"margin-top:5px;margin-bottom:15px;"}))
    
class UserRegisterForm(forms.Form):
    Username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control name" ,"placeholder":"Enter Your Username"}))
    Email=forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control mail","placeholder":"Type Your Email",'required':'True'}))
    Password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control pass","placeholder":"Enter Your Password"}))
    Confirm_password=forms.CharField(label="Confirm password",widget=forms.PasswordInput(attrs={"class":"form-control pass","placeholder":"Confirm Your Password"}))
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'class':'form-control', "placeholder":"Enter the captcha", 'style':"margin-top:5px;margin-bottom:15px;"}))
    
    class Meta:
        model = User
        fileds = ['email','username',]
    
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
        if Password is None:
            raise form.ValidationError("Enter some password.")
        if Password != Password2:
            raise forms.ValidationError("Passwords didn't match")
        return data

class UserAdminCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','username']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'username','password', 'is_active', 'admin']

    def clean_password(self):
        return self.initial["password"]
from django.db import models
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save,pre_save
from userinfo.models import UserInfo

# Create your models here.
# class Usermodel(models.Model,User):
#     def get_absolute_url(self):
#             return reverse('user_detail')

class UserManager(BaseUserManager):
    def create_user(self, username ,email, password=None):
        if not email or not username:
            raise ValueError('Users must have an email address and username')
        user = self.model(
            email=self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, email, password):
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self,username, email, password):
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    userInfo = models.OneToOneField(UserInfo,null=True,blank=True,on_delete=models.CASCADE)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # Email & Password are required by default.

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

class GuestUser(models.Model):
    email       =models.EmailField(null=False)
    timestamp   =models.DateTimeField( auto_now_add=True)
    update      =models.DateTimeField(auto_now=True)
    active      =models.BooleanField(default=True)

    def __str__(self):
        return self.email

def pre_save_Userinfo_binding(sender,instance,*args,**kwargs):
    if instance.userInfo is None:
        instance.userInfo = UserInfo.objects.create()
        
pre_save.connect(pre_save_Userinfo_binding,sender=User)
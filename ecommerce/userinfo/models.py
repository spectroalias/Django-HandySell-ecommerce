from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

user = get_user_model()

genders = (
        ('Male','male'),
        ('Female','female'),
        ('Other','other')
        )

class UserInfo(models.Model):
    user = models.ForeignKey(user,null=True,blank=True,on_delete=models.CASCADE)
    gender = models.CharField(choices=genders, max_length=10)
    contact= models.CharField(max_length=10,null=True,blank=True)
    profile_pic = models.ImageField(upload_to='User/Avatar')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
    
    def is_active(self):
        return self.active
    
    def make_inactive(self):
        self.active=False


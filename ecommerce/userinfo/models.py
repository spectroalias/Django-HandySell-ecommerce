from django.db import models
from django.db.models.signals import post_save,pre_save
# Create your models here.

genders = (
        ('Male','male'),
        ('Female','female'),
        ('Other','other')
        )

class UserInfo(models.Model):
    # user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    gender = models.CharField(null=True,blank=True,choices=genders, max_length=20)
    contact= models.CharField(max_length=12,null=True,blank=True)
    profile_pic = models.ImageField(upload_to='User/Avatar')

    def __str__(self):
        return str(self.id)


def pre_save_default_profilePic(sender,instance,*args,**kwargs):
    if not instance.profile_pic:
        instance.profile_pic='default.jpeg'
        

# def post_save_Userinfo_binding(sender,instance,*args,**kwargs):
#     userinfo_obj = UserInfo.objects.filter(user=instance,active=True)
#     if userinfo_obj.count()==0:
#         UserInfo.objects.create(user=instance)
        
# post_save.connect(post_save_Userinfo_binding,sender=User)
pre_save.connect(pre_save_default_profilePic,sender=UserInfo)

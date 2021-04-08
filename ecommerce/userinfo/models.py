from django.db import models
from django.db.models.signals import post_save,pre_save
import random
import os
# Create your models here.

genders = (
        ('Male','male'),
        ('Female','female'),
        ('Other','other')
        )

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "User/Avatar/{final_filename}".format(
            final_filename=final_filename
    )

class UserInfo(models.Model):
    gender = models.CharField(null=True,blank=True,choices=genders, max_length=20)
    contact= models.CharField(max_length=12,null=True,blank=True)
    profile_pic = models.ImageField(upload_to=upload_image_path)

    def __str__(self):
        return str(self.id)


def pre_save_default_profilePic(sender,instance,*args,**kwargs):
    if instance.profile_pic is None:
        instance.profile_pic='default.jpeg'
        
pre_save.connect(pre_save_default_profilePic,sender=UserInfo)

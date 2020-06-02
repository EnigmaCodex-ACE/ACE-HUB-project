from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import random
random_bios = ["Hey, I am new to Ace Students","Hello people","This is fun","I really need to change my bio"]


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.png',upload_to='profile_pics')
    bg_img = models.ImageField(default='default.jpg',upload_to='bg_pics')
    bio = models.TextField(default=random.choice(random_bios))
    def __str__(self):
        return f'{self.user}'

class CollegeDataBase(models.Model):
    #user = models.ForeignKey(User,on_delete=models.CASCADE)
    clg_name = models.CharField(User,default=" ",max_length=100)
    rollno = models.CharField(User,max_length=10,default="1XAG1A0XXX")
    is_cr = models.BooleanField(User,default=False)
    def __str__(self):
        return f'{self.rollno} Data'

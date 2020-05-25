from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import random
random_bios = ["Hey, I am new to Ace Students","Hello people","This is fun","I really need to change my bio"]


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.png',upload_to='profile_pics')
    bio = models.TextField(default=random.choice(random_bios))
    is_classrep = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if(img.height > 300 or img.width > 300):
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class CollegeDetails(models.Model):
    rollno = models.CharField(max_length=10,default="1XAG1A0XXX")
    

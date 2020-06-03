import random
import json
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class EducationalInstitution(models.Model):
    institution_name = models.CharField(max_length=100,unique=True)
    branch_available = models.CharField(null=True)
    stream_available = models.CharField(null=True)
    address = models.TextField(null=True)

    def __str__(self):
        return self.institution_name

class StudentProfile(models.Model):
    institution = models.ForeignKey(EducationalInstitution,on_delete=models.DO_NOTHING)
    branch = models.CharField(null=True)
    stream = models.CharField(null=True)
    rollno = models.CharField(max_length=15,null=True)
    is_cr = models.BooleanField(default=False)


class User(AbstractUser):

    RANDOM_BOIS = ["Hey, I am new to Ace Students","Hello people","This is fun","I really need to change my bio"]

    profile_pic = models.ImageField()
    bio_txt = models.TextField(default=random.choice(RANDOM_BOIS))
    student_profile = models.OneToOneField(StudentProfile, on_delete=models.PROTECT)

# class BRANCH_CHOICES(models.TextChoices):
#     ece = 'ece'
#     cse = 'cse'
#     mech = 'mech'
#     civil = 'civil'
#     chemical = 'chemical'
#     others = 'others'

# class STREAM_CHOICES(moels.TextChoices):
#     engineering = 'engineering'
#     others = 'others'

#abstract classes if change for email is required
class UserAbstractManagerEmail(BaseUserManager):
    """Define a model manager for model """
    use_in_migrations = True
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('The given mail is not valid')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password = None, **extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('for super user is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('for super user is_superuser = false')

        return self._create_user(email, password, **extra_fields)
    class Meta:
        abstract = True
    
class UserAbstractEmail(AbstractUser):
    username = None
    first_name = None
    last_name = None
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=False)
    phone_number = models.CharField(max_length=10, null = False, blank=False)
    # credit = models.ForeignKey(Credit, on_delete=models.CASCADE) 

    # objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        abstract = True
    
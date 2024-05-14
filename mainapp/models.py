from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
GENDER_CHOICES=(
    (None, 'sex:'),
    ('M','Male'),
    ('F','Female'),
    ('G','Gay'),
    ('L','Lesbian'))
class User(AbstractUser):
    addressess=models.CharField(max_length=100,verbose_name="addressline")
    number=models.IntegerField(default="05462",verbose_name="addressline")
    gender=models.CharField(choices=GENDER_CHOICES,max_length=2)
    
 

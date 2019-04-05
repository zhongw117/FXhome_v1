from django.db import models
from django.contrib.auth.models import AbstractBaseUser
class User(AbstractBaseUser):
    username = models.CharField(max_length=128, unique=True)
    password1 = models.CharField(max_length=256)
    password2 = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    c_time = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username
    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

class Hotel(models.Model):
    hotelname = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')

    class Meta:
        db_table = 'howdy_hotel'
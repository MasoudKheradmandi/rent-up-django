from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AdminInformation(models.Model):
    account = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    full_name = models.CharField(max_length=300,unique=True,)
    Email = models.EmailField(max_length=350)
    phone = models.CharField(max_length=11,unique=True,verbose_name="تلفن اول")
    phone_2 = models.CharField(max_length=11,null=True,blank=True, unique=True,verbose_name="تلفن دوم")
    semat = models.CharField(max_length=100,default='مشاور فروش',verbose_name="سمت")
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    code_posty = models.CharField(max_length=15,unique=True)
    image = models.ImageField(verbose_name="عکس")


    insta = models.CharField(max_length=500,unique=True,null=True,blank=True)
    whats_app = models.CharField(max_length=500,unique=True,null=True,blank=True)
    telegram = models.CharField(max_length=500,unique=True,null=True,blank=True)

    about_me = models.TextField()

    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name= 'مشاور'
        verbose_name_plural= 'اطلاعات کارکنان'
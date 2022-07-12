from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class aparteman(models.Model):
    STATUS_BUY = (
        ('برای خرید', 'برای خرید'),
        ('برای رهن و اجاره', 'برای رهن و اجاره'),
    )
    SANAD_CHOICES = (
        ('شش دانگ', 'شش دانگ'),
        ('مشاع', 'مشاع'),
        ('اصلاحات ارضی', 'اصلاحات ارضی'),
    )

    titr = models.CharField(max_length=150, verbose_name='تیتر')
    nevisande = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='نویسنده')
    
    status_buy = models.CharField(
        max_length=50, choices=STATUS_BUY, default='برای خرید', verbose_name='برای خرید/رهن و اجاره')
    gheymat = models.PositiveIntegerField(
        default=0, verbose_name='قیمت')
    gheymat_rahn = models.PositiveIntegerField(
        default=0, verbose_name='قیمت رهن')
    gheymat_ejare = models.PositiveIntegerField(
        default=0, verbose_name='قیمت اجاره')
    locations = models.TextField(verbose_name='ادرس اپارتمان')
    sanad = models.CharField(
        max_length=32, choices=SANAD_CHOICES, default='شش دانگ', verbose_name='نوع سند')
    andaze = models.PositiveSmallIntegerField(verbose_name='متراژ')
    tabaghe = models.CharField(max_length=2, verbose_name='طبقه')
    tedad_tabaghe = models.PositiveSmallIntegerField(verbose_name='تعداد طبقه')
    tedad_vahed_tabaghe = models.PositiveSmallIntegerField(
        verbose_name='تعداد واحد در هر طبقه')
    tedad_otagh = models.CharField(max_length=2, verbose_name='تعداد اتاق')
    tedad_dastshoe = models.PositiveSmallIntegerField(
        verbose_name='تعداد سرویس بهداشتی')
    sal_sakht = models.PositiveSmallIntegerField(verbose_name='چند سال ساخت')
    ghabel_moaveze = models.BooleanField(
        default=False, verbose_name='قابل معاوضه؟')
    tozihat_karbar = models.TextField(verbose_name='توضیحات کاربر')
    tozihat_khososy = models.TextField(
        blank=True, null=True, verbose_name='توضیحات خصوصی')
    # map_1 = models.TextField(blank=True, null=True, verbose_name='نقشه گوگل')
    image = models.ImageField(verbose_name='عکس اصلی')
    upload_time = models.DateField(
        default=timezone.now, verbose_name='زمان ثبت')
    vise = models.BooleanField(default=False, verbose_name='ویژه؟')
    active = models.BooleanField(default=True, verbose_name='نمایش داده شود؟')
    
    
    #--------------------BooleanField
    tahvie = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    trass = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    bed = models.BooleanField(default=False)
    micro = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    sahel = models.BooleanField(default=False)
    system_garmayeshi= models.BooleanField(default=False)
    sigary = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    #-----------------------    
    def __str__(self):
        return self.titr

    class Meta:
        ordering = ['-upload_time']
        verbose_name = 'اپارتمان'
        verbose_name_plural = 'اپارتمان ها'
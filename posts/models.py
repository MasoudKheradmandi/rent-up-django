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
    SAL_SAKHT = (
        ('0-5','0-5'),
        ('5-10','5-10'),
        ('10-20','10-20'),
        ('20+','20+')
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
    andaze = models.PositiveSmallIntegerField(verbose_name='متراژ',default=0)
    tabaghe = models.PositiveIntegerField(verbose_name='طبقه')
    tedad_tabaghe = models.PositiveSmallIntegerField(verbose_name='تعداد طبقه')
    tedad_vahed_tabaghe = models.PositiveSmallIntegerField(
        verbose_name='تعداد واحد در هر طبقه',default=0)
    tedad_otagh = models.CharField(max_length=2, verbose_name='تعداد اتاق')
    tedad_dastshoe = models.PositiveSmallIntegerField(
        verbose_name='تعداد سرویس بهداشتی')
    sal_sakht = models.CharField(max_length=10, choices=SAL_SAKHT,default="0-5")
    ghabel_moaveze = models.BooleanField(
        default=False, verbose_name='قابل معاوضه؟')
    tozihat_karbar = models.TextField(verbose_name='توضیحات کاربر')
    tozihat_khososy = models.TextField(
        blank=True, null=True, verbose_name='توضیحات خصوصی')
    # map_1 = models.TextField(blank=True, null=True, verbose_name='نقشه گوگل')
    image = models.ImageField(verbose_name='عکس اصلی',null=True)
    upload_time = models.DateField(
        default=timezone.now, verbose_name='زمان ثبت')
    parking = models.CharField(max_length=2,null=True)
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
    #-----------------------    
    def __str__(self):
        return self.titr

    class Meta:
        ordering = ['-upload_time']
        verbose_name = 'اپارتمان'
        verbose_name_plural = 'اپارتمان ها'

class aparteman_images(models.Model):
    place = models.ForeignKey('aparteman',on_delete=models.CASCADE)
    images = models.ImageField()


class vilae(models.Model):
    SAL_SAKHT = (
        ('0-5','0-5'),
        ('5-10','5-10'),
        ('10-20','10-20'),
        ('20+','20+')
    )
    STATUS_BUY = (
        ('برای خرید', 'برای خرید'),
        ('برای اجاره', 'برای اجاره'),
    )
    SANAD_CHOICES = (
        ('شش دانگ', 'شش دانگ'),
        ('مشاع', 'مشاع'),
        ('اصلاحات ارضی', 'اصلاحات ارضی'),
    )

    titr = models.CharField(max_length=300, verbose_name="تیتر")
    nevisande = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="نویسنده")
    
    status_buy = models.CharField(
        max_length=50, choices=STATUS_BUY, default='برای خرید', verbose_name="برای خرید/رهن و اجاره")
    gheymat = models.BigIntegerField(
        default=0, verbose_name="قیمت")
    gheymat_rahn = models.PositiveIntegerField(
       default=0, verbose_name="قیمت رهن")
    gheymat_ejare = models.PositiveIntegerField(
        default=0, verbose_name="قیمت اجاره")
    locations = models.TextField(verbose_name="ادرس ویلا")
    sanad = models.CharField(
        max_length=32, choices=SANAD_CHOICES, default='شش دانگ', verbose_name="نوع سند")
    andaze_zamin = models.PositiveSmallIntegerField(verbose_name="اندازه زمین")
    andaze_bana = models.PositiveSmallIntegerField(verbose_name="اندازه بنا")
    tedad_otagh = models.PositiveSmallIntegerField(
        verbose_name="تعداد اتاق")
    tedad_dastshoe = models.PositiveSmallIntegerField(
        verbose_name="تعداد سرویس بهداشتی")
    sal_sakht = models.CharField(max_length=10, choices=SAL_SAKHT,default="0-5")
    ghabel_moaveze = models.BooleanField(
        default=False, verbose_name="قابل معاوضه؟")
    tozihat_karbar = models.TextField(verbose_name="توضیحات کاربر")
    tozihat_khososy = models.TextField(
        blank=True, null=True, verbose_name="توضیحات خصوصی")
    map_1 = models.TextField(blank=True, null=True, verbose_name="نقشه گوگل")
    image = models.ImageField(verbose_name="عکس اصلی",null=True)
    upload_time = models.DateField(
        default=timezone.now, verbose_name="زمان ثبت")
    vise = models.BooleanField(default=False, verbose_name="ویژه؟")
    active = models.BooleanField(default=True, verbose_name="نمایش؟")
    parking = models.CharField(max_length=2,null=True)



        
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
    #-----------------------    

    class Meta:
        ordering = ['-upload_time']
        verbose_name = 'ویلا'
        verbose_name_plural = 'ویلاها'

    def __str__(self):
        return self.titr

class vilae_image(models.Model):
    place =models.ForeignKey('vilae',on_delete=models.CASCADE)
    images = models.ImageField()

    def __str__(self):
        return self.place.titr
    

    

class zamin(models.Model):
    SANAD_CHOICES = (
        ('شش دانگ', 'شش دانگ'),
        ('مشاع', 'مشاع'),
        ('اصلاحات ارضی', 'اصلاحات ارضی'),
    )
    ZAMIN_CHOICES = (
        ('تفریحی توریستی', 'تفریحی توریستی'),
        ('باغ', 'باغ'),
        ('مسکونی', 'مسکونی'),
    )
    titr = models.CharField(max_length=150, verbose_name='تیتر')
    nevisande = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='نویسنده')
    gheymat = models.PositiveIntegerField(verbose_name='قیمت')
    andaze = models.PositiveSmallIntegerField(verbose_name=' اندازه')
    noe_zamin = models.CharField(
        max_length=30, choices=ZAMIN_CHOICES, default='مسکونی',verbose_name='نوع زمین')
    locations = models.TextField(verbose_name='ادرس زمین')
    sanad = models.CharField(
        max_length=32, choices=SANAD_CHOICES, default='شش دانگ', verbose_name='نوع سند')
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

    def __str__(self):
        return self.titr

    class Meta:
        ordering = ['-upload_time']
        verbose_name = 'زمین'
        verbose_name_plural = 'زمین ها'
    
class zamin_image(models.Model):
    place = models.ForeignKey('zamin',on_delete=models.CASCADE)
    images = models.ImageField()
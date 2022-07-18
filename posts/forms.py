from django import forms
from .models import aparteman_images


class SaveFormAparteman(forms.Form):
    STATUS_BUY = (
        ('برای خرید', 'برای خرید'),
        ('برای رهن و اجاره', 'برای رهن و اجاره'),
    )
    SAL_SAKHT = (
        ('0-5','0-5'),
        ('5-10','5-10'),
        ('10-20','10-20'),
        ('20+','20+')
    )
    SANAD_CHOICES = (
        ('شش دانگ', 'شش دانگ'),
        ('مشاع', 'مشاع'),
        ('اصلاحات ارضی', 'اصلاحات ارضی'),
    )
    titr = forms.CharField(max_length=150)
    status_buy = forms.ChoiceField(choices = STATUS_BUY)
    gheymat = forms.IntegerField()
    gheymat_rahn = forms.IntegerField()
    gheymat_ejare = forms.IntegerField()
    locations = forms.CharField(max_length=3000)
    sanad = forms.ChoiceField(choices=SANAD_CHOICES,)
    andaze = forms.IntegerField()
    tabaghe = forms.IntegerField()
    tedad_tabaghe = forms.IntegerField()
    tedad_vahed_tabaghe = forms.IntegerField()
    tedad_otagh = forms.IntegerField()
    tedad_dastshoe = forms.IntegerField()
    sal_sakht = forms.ChoiceField(choices=SAL_SAKHT)
    ghabel_moaveze = forms.BooleanField(required=False)
    tozihat_karbar = forms.CharField(widget=forms.Textarea())
    tozihat_khososy = forms.CharField(widget=forms.Textarea())
    # map_1 = 
    image = forms.ImageField()
    active = forms.BooleanField(required=False)
    
    
    #-----------------------------
    tahvie = forms.BooleanField(required=False)
    internet = forms.BooleanField(required=False)
    trass = forms.BooleanField(required=False)
    wifi = forms.BooleanField(required=False)
    bed = forms.BooleanField(required=False)
    micro = forms.BooleanField(required=False)
    balcony = forms.BooleanField(required=False)
    sahel = forms.BooleanField(required=False)
    system_garmayeshi= forms.BooleanField(required=False)
    sigary = forms.BooleanField(required=False)
    parking = forms.BooleanField(required=False)
    #-----------------------------------------



        
class SavePostvillae(forms.Form):
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
        ('اصلاخات ارضی', 'اصلاحات ارضی'),
    )
    titr = forms.CharField(max_length=300)
    status_buy = forms.ChoiceField(choices = STATUS_BUY)
    gheymat = forms.IntegerField()
    gheymat_rahn = forms.IntegerField()
    gheymat_ejare = forms.IntegerField()
    locations = forms.CharField(max_length=3000)
    sanad = forms.ChoiceField(choices=SANAD_CHOICES)
    andaze_zamin = forms.IntegerField()
    andaze_bana=forms.IntegerField()
    tedad_otagh = forms.IntegerField()
    tedad_dastshoe = forms.IntegerField()
    sal_sakht = forms.ChoiceField(choices=SAL_SAKHT)
    ghabel_moaveze = forms.BooleanField(required=False)
    tozihat_karbar = forms.CharField(widget=forms.Textarea())
    tozihat_khososy = forms.CharField(widget=forms.Textarea())
    # map_1 = 
    image = forms.ImageField()
    active = forms.BooleanField(required=False)



    #-----------------------------
    parking = forms.BooleanField()
    tahvie = forms.BooleanField(required=False)
    internet = forms.BooleanField(required=False)
    trass = forms.BooleanField(required=False)
    wifi = forms.BooleanField(required=False)
    bed = forms.BooleanField(required=False)
    micro = forms.BooleanField(required=False)
    balcony = forms.BooleanField(required=False)
    sahel = forms.BooleanField(required=False)
    system_garmayeshi= forms.BooleanField(required=False)
    sigary = forms.BooleanField(required=False)
    #-----------------------------------------

class vilae_image_form(forms.Form):
    images = forms.ImageField()



class SavePostZamin(forms.Form):
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
    titr = forms.CharField(max_length=150)
    gheymat = forms.IntegerField()
    andaze = forms.IntegerField()
    noe_zamin = forms.ChoiceField(choices=ZAMIN_CHOICES)
    locations = forms.CharField(widget=forms.Textarea())
    sanad=forms.ChoiceField(choices=SANAD_CHOICES)
    ghabel_moaveze = forms.BooleanField(required=False)
    tozihat_karbar=forms.CharField(widget=forms.Textarea())
    tozihat_khososy=forms.CharField(widget=forms.Textarea())
    image = forms.ImageField()
    active = forms.BooleanField(required=False)

class zamin_image_form(forms.Form):
    images = forms.ImageField()
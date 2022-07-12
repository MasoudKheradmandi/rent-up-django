from email.policy import default
from secrets import choice
from django import forms
from matplotlib import image

class SaveFormAparteman(forms.Form):
    STATUS_BUY = (
        ('برای خرید', 'برای خرید'),
        ('برای رهن و اجاره', 'برای رهن و اجاره'),
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
    sal_sakht = forms.IntegerField()
    ghabel_moaveze = forms.BooleanField(required=False)
    tozihat_karbar = forms.CharField(max_length=500)
    tozihat_khososy = forms.CharField(max_length=500)
    # map_1 = 
    image = forms.ImageField()
    active = forms.BooleanField(required=False)

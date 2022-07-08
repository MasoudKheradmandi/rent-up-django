from enum import unique
from django import forms


class UserAccountForm(forms.Form):
    full_name = forms.CharField(max_length=300)
    Email = forms.EmailField(max_length=254)
    phone = forms.CharField(max_length=11)
    phone_2 = forms.CharField(max_length=11,required=False)
    semat = forms.CharField(max_length=100)
    address = forms.CharField(max_length=300)
    city = forms.CharField(max_length=300)
    code_posty = forms.CharField(max_length=15)

    insta = forms.CharField(max_length=500,required=False)
    whats_app = forms.CharField(max_length=500,required=False)
    telegram = forms.CharField(max_length=500,required=False)


    about_me = forms.CharField(widget=forms.Textarea)



    #will be complate
    
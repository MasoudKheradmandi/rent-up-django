from django import forms


class CommentFormAparteman(forms.Form):
    Full_name = forms.CharField(max_length=250)
    Email_address = forms.EmailField(max_length=254)
    message = forms.CharField(widget=forms.Textarea())

class CommentFormVillae(forms.Form):
    Full_name = forms.CharField(max_length=250)
    Email_address = forms.EmailField(max_length=254)
    message = forms.CharField(widget=forms.Textarea())
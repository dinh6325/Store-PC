from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'image', 'stock']


class CheckoutForm(forms.Form):
    full_name   = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    address     = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class':'form-control'}))
    city        = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    postal_code = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
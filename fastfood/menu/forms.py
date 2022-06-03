from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'about', 'category', 'picture', 'price')


class ProductFormUpdate(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'about', 'category', 'price')

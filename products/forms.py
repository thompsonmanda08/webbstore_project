from django import forms
from .models import Product

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'stock',
           'description',
            'img_url',
        ]
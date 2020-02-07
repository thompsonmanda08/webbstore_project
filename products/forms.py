from django import forms
from .models import Product

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'price',
            'stock',
           'description',
            'image',

        ]
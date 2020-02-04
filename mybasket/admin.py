from django.contrib import admin
from .models import MyBasketItem

# Configure your ModelDisplay here

#class MyBasketItemAdmin:
 #   List_display = ('name', 'price', 'seller', 'sellerID')

# Register your models here.
admin.site.register(MyBasketItem)
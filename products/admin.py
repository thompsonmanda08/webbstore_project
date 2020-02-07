from django.contrib import admin
from .models import Product, Offer, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'id')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.

admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

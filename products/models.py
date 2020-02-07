from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    image_url = models.CharField(max_length=1000, default=None, blank=True)

    def __str__(self):
        return self.name[:100]

class Offer(models.Model):
    code = models.CharField(max_length=7)
    description = models.TextField(blank=True)
    discount = models.FloatField()

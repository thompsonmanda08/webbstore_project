# Generated by Django 3.0.2 on 2020-02-06 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0005_auto_20200206_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyBasketItem',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.Product')),
            ],
            bases=('products.product',),
        ),
    ]
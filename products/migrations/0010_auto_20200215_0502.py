# Generated by Django 3.0.2 on 2020-02-15 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200212_0829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='offer',
            name='discount',
            field=models.FloatField(blank=True),
        ),
    ]

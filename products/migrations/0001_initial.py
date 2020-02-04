# Generated by Django 2.2.5 on 2019-09-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField(max_length=20)),
                ('stock', models.IntegerField()),
                ('img_url', models.CharField(max_length=2083)),
            ],
        ),
    ]

# Generated by Django 5.1 on 2024-08-12 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='brand',
        ),
        migrations.DeleteModel(
            name='Brands',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]

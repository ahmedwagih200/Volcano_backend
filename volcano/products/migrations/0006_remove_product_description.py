# Generated by Django 3.2 on 2022-03-08 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
from django.db import models
from customer.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='categories', default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, null=True)
    price = models.IntegerField(default=0, null=True)
    # description = models.CharField(max_length=350, null=True)
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price_id = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    # state=models.ForeignKey('Status', on_delete=models.CASCADE)
    user = models.ForeignKey('customer.User', on_delete=models.CASCADE, null=True)
    # delivery=models.ForeignKey('Delivery_man', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    total = models.IntegerField(default=0, null=True)


class order_item(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0, null=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True)


class Delivery_man(models.Model):
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=15)

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='categories', default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, null=True)
    price = models.IntegerField(default=0, null=True)
    description = models.CharField(max_length=350, null=True)
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class Order(models.Model):
#     state=models.ForeignKey('Status', on_delete=models.CASCADE)
#     user=models.ForeignKey('Customer', on_delete=models.CASCADE)
#     delivery=models.ForeignKey('Delivery_man', on_delete=models.CASCADE)
#     date=models.DateTimeField(auto_now_add=True)


# class order_product(models.Model):
#     order=models.ForeignKey('Order', on_delete=models.CASCADE)
#     product=models.ForeignKey('Product', on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('order', 'product')


# class Status(models.Model):
#     name = models.CharField(max_length=60)

#     def __str__(self):
#         return self.name


class Delivery_man(models.Model):
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=15)




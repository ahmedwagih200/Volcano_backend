
from django.db import models
from customer.models import User
from django.core.validators import RegexValidator
#from .forms import cate_form
from django import forms

# class cate_form(forms.Form):

#     name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     image = forms.ImageField()
    





class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='categories', default=None, blank=True, null=True)
    
    # dic={'name': name , 'image':image}  
    # @property
    # def form(self):
    #     form1=cate_form(self.dic ) 
    #     return form1  



    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, null=True)
    price = models.IntegerField(default=0, null=True)
    #description = models.CharField(max_length=350, null=True)
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    #price_id = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    
    state=models.ForeignKey('Status', on_delete=models.CASCADE , null=True)
    user=models.ForeignKey('customer.User', on_delete=models.CASCADE , null=True)
    #delivery=models.ForeignKey('Delivery_man', on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    address=models.CharField(max_length=350, null=True)
    payment=models.CharField(max_length=200, null=True)
    total = models.IntegerField(default=0, null=True)
    phone_regex = RegexValidator(regex=r'^01[1|0|2|5][0-9]{8}$', message='phone must be an egyptian phone number...')
    phone = models.CharField(null=False, validators=[phone_regex], max_length=14 )
    
    

    @property
    def get_items(self):
        items=self.order_item_set.all()
        return items


class order_item(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0, null=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True)
    



    #total = models.IntegerField(default=0, null=True)


#     class Meta:
#         unique_together = ('order', 'product')


class Status(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


# class Delivery_man(models.Model):
#     name = models.CharField(max_length=60)
#     phone = models.CharField(max_length=15)




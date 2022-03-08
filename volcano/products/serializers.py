from dataclasses import fields
from rest_framework import serializers
from .models import *


class prod_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class cate_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class order_serializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model = Order
        fields = '__all__'

class order_item_serializer(serializers.ModelSerializer):
    item=prod_serializer()
    class Meta:
        model = order_item
        fields = ['item' , 'qty']


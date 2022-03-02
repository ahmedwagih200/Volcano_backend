from dataclasses import fields
from rest_framework import serializers
from .models import Product, Category


class prod_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class cate_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

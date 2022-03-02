from django.shortcuts import render

# Create your views here.
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_product(req, id):
    prod = Product.objects.filter(category_id=id)
    serializer = prod_serializer(prod, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_category(req):
    cate = Category.objects.all()
    serializer = cate_serializer(cate, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_cate(req, id):
    c = Category.objects.get(id=id)
    serializer = cate_serializer(c)
    return Response(serializer.data)

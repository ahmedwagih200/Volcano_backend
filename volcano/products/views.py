from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from customer.models import User


@api_view(['GET'])
def get_product(req, id):
    prod = Product.objects.filter(category_id=id)
    serializer = prod_serializer(prod, many=True)
    print(serializer.data)

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


@api_view(['POST'])
def create_order(req ):
    print(req.data)
    user=User.objects.get(id=req.data['user'])
    s=Status.objects.get(id=1)
    if req.data['cash'] == True :
        order= Order.objects.create(total=req.data['price'] , user=user , address=req.data['address'] , phone=req.data['phone'] , payment='cash on delivery' , state=s)

    else:
        order= Order.objects.create(total=req.data['price'] , user=user , address=req.data['address'] , phone=req.data['phone'] , payment='pay online' , state=s)

    arr=req.data['items']
    for p in arr:
        item=Product.objects.get(id=p['id'])
        order_item.objects.create(order=order , item=item , qty=p['qty'] )
    return Response(req.data)


@api_view(['GET'])
def get_orders(req  , id):
    user=User.objects.get(id=id)
    orders=user.order_set.all()
    serializer = order_serializer(orders, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def get_order(req  , id):
    ord=Order.objects.get(id=id)
    order=ord.order_item_set.all()
    
    serializer = order_item_serializer(order, many=True)
    
    return Response(serializer.data)



@api_view(['GET'])
def get_product_payment(req, id):
    prod = Product.objects.filter(id=id)
    serializer = prod_serializer(prod, many=True)

    return Response(serializer.data)


    
# def test(req , id ):
#     Order.objects.filter(id=id).delete()
#     return HttpResponse('deleted')

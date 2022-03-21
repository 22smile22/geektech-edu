# from django.shortcuts import render
# # Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
from products.serializers import ProductValidateSerializer #ls4
from products.models import Product, Review
from rest_framework import status


@api_view(['GET'])
def test(request):
    data = {
        'text': 'Hello World!',
        'int': 100,
        'float': 2.99,
        'list': [1, 2, 3, 4],
        'bool': False
    }
    return Response(data=data)

#ls3
@api_view(['POST'])
def test_post(request):
    print(request.data['name'])
    print(request.data.get('name')) #--более предпочтит использовать
    return Response(data={'message': 'OK'})

# @api_view(['GET']) #ls2
# def product_list_view(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(data=serializer.data)

@api_view(['GET', 'POST']) #ls3
def product_list_create_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
       serializer = ProductValidateSerializer(data=request.data) #ls4
       if not serializer.is_valid():
           return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                           data={'errors' : serializer.errors})
       # title = request.data.get('title')
       title = serializer.validated_data.get('title')
       # if title is None: #ls4
       #     title = ''
       # if len(title) < 2: #ls4
       #     return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
       #                     data={'error': 'title length less than 2'})
       weight = request.data.get('weight')
       price = request.data.get('price')
       is_stock = request.data.get('is_stock')
       valid_until = request.data.get('valid_until')
       brand_id = request.data.get('brand_id')
       # product = Product.objects.create(**serializer.validated_data)
       product = Product.objects.create(title = title, weight = weight,
                                        price = price, is_stock= is_stock,
                                        valid_until = valid_until,
                                        brand_id = brand_id)
       for i in serializer.validated_data['reviews']:
           Review.objects.create(product=product, text=i['text'], stars=i['stars'])
       return Response(data=ProductSerializer(product).data)

# @api_view(['GET']) #ls2
# def product_item_view(request, id):
#     try:
#         product = Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         return Response(data={'error': 'Product not Found!!!'},
#                         status=status.HTTP_404_NOT_FOUND)
#                         # status=404)
#     serializer = ProductSerializer(product)
#     return Response(data=serializer.data)

#ls3
@api_view(['GET', 'PUT', 'DELETE'])
def product_item_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Product not Found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
                        # status=404)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(data={'message': 'Product removed'})
    else:
        product.title = request.data.get('title')
        product.weight = request.data.get('weight')
        product.price = request.data.get('price')
        product.is_stock = request.data.get('is_stock')
        product.valid_until = request.data.get('valid_until')
        product.brand_id = request.data.get('brand id')
        product.save()
        return Response(data=ProductSerializer(product).data)


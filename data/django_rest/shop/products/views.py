# from django.shortcuts import render
# # Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
from products.models import Product
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

@api_view(['GET'])
def product_list_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def product_item_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Product not Found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
                        # status=404)
    serializer = ProductSerializer(product)
    return Response(data=serializer.data)

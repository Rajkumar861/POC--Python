from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.serializers import Serializer
from .serializer import Productserializer
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def welcome_note(request):
    return HttpResponse("<h1>Welcome to the Poduct Management....</h1>")

@api_view(['GET','POST'])
def product_list(request):

    if request.method == 'GET':
        product = Product.objects.all()
        Serializer = Productserializer(product, many=True)
        return Response(Serializer.data)

    elif request.method == 'POST':
        Serializer = Productserializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def update_product(request,id):
    
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Serializer = Productserializer(product)
        return Response(Serializer.data)

    elif request.method == 'PUT':
        Serializer = Productserializer(instance=product,data=request.data,partial=True)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data)
        return Response(Serializer.error,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response('Item deleted successfully....')


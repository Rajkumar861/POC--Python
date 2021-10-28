from django.db.models import fields
from .models import Product
from rest_framework import serializers

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'
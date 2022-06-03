from rest_framework import serializers
from menu.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'about', 'category', 'picture', 'price')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('title', 'user', 'product', 'amount', 'date', 'status')


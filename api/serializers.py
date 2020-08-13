from rest_framework import serializers
from store.models.order import Order
from store.models.product import Product
from store.models.customer import Customer

from django.contrib.auth.hashers import make_password

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'image']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product', 'customer', 'quantity', 'price', 'date', 'completed']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'email']

class CostumerCreateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        customer = Customer()
        customer.name = validated_data.get('name')
        customer.email = validated_data.get('email')
        customer.phone = validated_data.get('phone')
        customer.password = make_password(validated_data.get('password'))
        customer.save()
        return customer

    def validate_user(self, data):
        customer = Customer.objects.filter(email = data)
        if(customer):
            raise serializers.ValidationError('This email is already in use')
        else:
            return data




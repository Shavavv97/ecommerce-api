from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import CustomerSerializer, ProductSerializer, OrderSerializer, CostumerCreateSerializer
from store.models.order import Order
from store.models.product import Product
from store.models.customer import Customer

class ProductAPI(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class UserAPI(ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class UserCreateAPI(APIView):
    def post(self, request):
        serializer = CostumerCreateSerializer(data = request.data)
        if (serializer.is_valid()):
            customer = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

class OrderAPI(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
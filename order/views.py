from .models import *
from order.serializers import *
from rest_framework import generics


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MealList(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class TableList(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ServicePercentageList(generics.ListCreateAPIView):
    queryset = ServicePercentage
    serializer_class = ServicePercentageSerializer


class CheckList(generics.ListCreateAPIView):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer


class StatusList(generics.ListCreateAPIView):
    queryset = Status
    serializer_class = StatusSerializer


class MealOrdersList(generics.ListCreateAPIView):
    queryset = MealOrders
    serializer_class = MealOrdersSerializer

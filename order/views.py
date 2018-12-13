from .models import *
from order.serializers import *
from rest_framework import generics


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department
    serializer_class = DepartmentSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category
    serializer_class = CategorySerializer


class MealList(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    #filtering in serializers
    # def get_queryset(self,*args, **kwargs):
    #     queryset_list = Meal.objects.all()
    #     query = self.request.GET.get("q")
    #     if query:
    #         queryset_list = queryset_list.filter(name__icontains=query).distinct()
    #     return queryset_list


class MealDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal
    serializer_class = MealSerializer


class TableList(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table
    serializer_class = TableSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order
    serializer_class = OrderSerializer


class ServicePercentageList(generics.ListCreateAPIView):
    queryset = ServicePercentage
    serializer_class = ServicePercentageSerializer


class ServicePercentageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicePercentage
    serializer_class = ServicePercentageSerializer


class CheckList(generics.ListCreateAPIView):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer


class CheckDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Check
    serializer_class = CheckSerializer


class StatusList(generics.ListCreateAPIView):
    queryset = Status
    serializer_class = StatusSerializer


class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status
    serializer_class = StatusSerializer


class MealOrdersList(generics.ListCreateAPIView):
    queryset = MealOrders.objects.all()
    serializer_class = MealOrdersSerializer


class MealOrdersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MealOrders
    serializer_class = MealOrdersSerializer


#Permissions in DRF
# from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
#     permission_class = [IsAuthenticatedOrReadOnly]


from .models import *
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'department')


class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = ('id', 'name', 'category', 'price', 'description')


class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = ('id', 'name')


class OrderSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'waiter', 'table', 'meals')


class ServicePercentageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicePercentage
        fields = ('id', 'percentage')


class CheckSerializer(serializers.ModelSerializer):
    total_sum = serializers.SerializerMethodField()
    #meals = serializers.SerializerMethodField()

    def get_total_sum(self, obj):
        summ = 0
        f = obj.order.meals.all().aggregate(Sum('price'))
        for i in f:
            summ += int(f.get('price__sum'))
            return summ
    #
    # def get_meals(self, obj):
    #     meals = obj.order.meals.objects.all()
    #     return meals

    class Meta:
        model = Check
        fields = ('id', 'order', 'date', 'service_fee', 'total_sum')
        depth = 0

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('id', 'name', 'order')


class MealOrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealOrders
        fields = ('id', 'meal', 'order')





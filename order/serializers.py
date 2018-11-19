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
    #order = OrderSerializer()
    total_sum = serializers.SerializerMethodField()
    #meals = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())

    def get_total_sum(self, obj):
        summ = 0
        meal_orders = MealOrders.objects.filter(order=obj.order)
        for meal_order in meal_orders:
            summ += meal_order.count * meal_order.meal.price
        return summ

    class Meta:
        model = Check
        fields = ('id', 'order', 'date', 'service_fee', 'total_sum')
        depth = 0



    # def to_representation(self, instance):
    #     representation = super(CheckSerializer, self).to_representation(instance)
    #     representation['meals'] = OrderSerializer(instance.order.meals).data
    #     return representation


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('id', 'name', 'order')


class MealOrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealOrders
        fields = ('id', 'meal', 'order')





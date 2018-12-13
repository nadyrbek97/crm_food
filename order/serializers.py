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


class MealRepresentationSerializer(serializers.BaseSerializer):

    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        meal_count = MealOrders.objects.filter(meal=obj.meal)
        count = meal_count.count
        print(count)
        return count

    def to_representation(self, obj):
        return {
            'id': obj.id,
            'name': obj.name,
            'count': obj.count
        }


class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = ('id', 'name')


class OrderSerializer(serializers.ModelSerializer):
    meals = MealRepresentationSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'waiter', 'table', 'meals')

    def create(self, validated_data):
        meals_data = validated_data.pop('meals')

        order = Order.objects.create(**validated_data)
        for meals in meals_data:
            m = Meal.objects.create(order=order, **meals)
            MealOrders.objects.create(order=order, meal=m)
        return order


class ServicePercentageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicePercentage
        fields = ('id', 'percentage')


class CheckSerializer(serializers.ModelSerializer):
    total_sum = serializers.SerializerMethodField()
    meals = serializers.SerializerMethodField()

    def get_total_sum(self, obj):
        summ = 0
        meal_orders = MealOrders.objects.filter(order=obj.order)
        for meal_order in meal_orders:
            summ += meal_order.count * meal_order.meal.price
        return summ

    def get_meals(self, obj):
        meal_order = Meal.objects.filter(order=obj.order)
        serializer = MealSerializer(meal_order, many=True)
        print(serializer)
        return serializer.data

    class Meta:
        model = Check
        fields = ('id', 'order', 'date', 'service_fee', 'total_sum', 'meals')


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('id', 'name', 'order')


class MealOrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealOrders
        fields = ('id', 'meal', 'order', 'count')

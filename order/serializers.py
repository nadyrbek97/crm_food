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


# class MealRepresentationSerializer(serializers.BaseSerializer):
#
#     count = serializers.SerializerMethodField()
#
#     def get_count(self, obj):
#         meal_count = MealOrders.objects.filter(meal=obj.meal)
#         count = meal_count.count
#         print(count)
#         return count
#
#     def to_representation(self, obj):
#         return {
#             'id': obj.id,
#             'name': obj.name,
#             'count': obj.count
#         }


class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = ('id', 'name')


class MealOrdersSerializer(serializers.ModelSerializer):
    # name = serializers.SerializerMethodField(required=False)

    class Meta:
        model = MealOrders
        fields = ('id', 'order_id', 'meal_id','count')

    # def get_name(self, obj):
    #     meal_order = Meal.objects.filter(order=obj.order)
    #     for meal in meal_order:
    #         name = name
    #     return name


class OrderSerializer(serializers.ModelSerializer):
    meals = MealOrdersSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'waiter', 'table', 'meals')

    def create(self, validated_data):
        # here we are taking out parameters of meal_order object
        meals_data = validated_data.pop('meals')
        # print(meals_data['count'])
        print(validated_data)
        # we have to create order object with **validated_data
        order = Order.objects.create(**validated_data)
        # I take by default meal with id 1 => must be changed
        meal = Meal.objects.get(id=1)
        for meals in meals_data:
            # creating mealorders objects
            MealOrders.objects.create(order=order, meal=meal, count=meals['count'])
        return order
    """
        validated_data -> json.file that we get after post method 
        
    """


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




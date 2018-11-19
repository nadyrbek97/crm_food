from django.db import models
from user.models import User
from django.db.models import Sum, Count


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='meals')
    price = models.IntegerField()
    description = models.TextField(max_length=800)

    def __str__(self):
        return self.name


#----------------------------------------------
class Table(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    waiter = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='orders')
    meals = models.ManyToManyField(Meal, through='MealOrders')

    def __str__(self):
        return "Order #" + str(self.pk) + "," + self.table.name + \
               ", Waiter: " + self.waiter.first_name + ", " \
                "Meals: " + str(self.meals.name)


class ServicePercentage(models.Model):
    percentage = models.IntegerField()

    def __str__(self):
        return str(self.percentage)


class Check(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateTimeField()
    service_fee = models.ForeignKey(ServicePercentage, on_delete=models.CASCADE)
    total_sum = models.IntegerField(null=True)

    def __str__(self):
        return "Check #" + str(self.pk)


class Status(models.Model):
    name = models.CharField(max_length=100)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.name


#------------------   ----------------------------
class MealOrders(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    count = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = 'MealToOrders'

    def __str__(self):
        return "Waiter: " + self.order.waiter.first_name + ", Meal: " + self.meal.name

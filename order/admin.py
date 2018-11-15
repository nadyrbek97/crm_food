from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Department)
admin.site.register(Category)
#admin.site.register(Meal)
admin.site.register(Table)
#admin.site.register(Order)
admin.site.register(ServicePercentage)
admin.site.register(Check)
admin.site.register(Status)
admin.site.register(MealOrders)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ['id']


class MealAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


admin.site.register(Order, OrderAdmin)
admin.site.register(Meal, MealAdmin)

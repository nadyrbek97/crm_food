from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from order import views

urlpatterns = [
    path('departments/', views.DepartmentList.as_view(), name='departments'),
    path('categories/', views.CategoryList.as_view()),
    path('meals/', views.MealList.as_view()),
    path('tables/', views.TableList.as_view()),
    path('orders/', views.OrderList.as_view()),
    path('checks/', views.CheckList.as_view()),
    path('mealorders/', views.MealOrdersList().as_view()),
    # Detail views
    path('departments/<int:pk>/', views.DepartmentDetail.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('meals/<int:pk>/', views.MealDetail.as_view()),
    path('tables/<int:pk>/', views.TableDetail.as_view()),
    path('orders/<int:pk>/', views.OrderDetail.as_view()),
    path('checks/<int:pk>/', views.CheckDetail.as_view()),
    path('mealorders/<int:pk>/', views.MealOrdersDetail().as_view()),
    # path('courses/<int:pk>/', views.CourseDetail.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

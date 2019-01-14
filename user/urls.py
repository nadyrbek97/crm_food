from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user import views
from .views import logout, register_view, login_view

urlpatterns = [
    path('users/login/', login_view),
    path('users/register/', register_view),
    path('users/logout/', logout),
    path('roles/', views.RoleList.as_view()),
    path('roles/<int:pk>', views.RoleDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

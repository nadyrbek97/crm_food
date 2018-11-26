from .models import *
from rest_framework import serializers


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    #first_name = serializers.CharField(read_only=True, source="user.first_name")
    #last_name = serializers.CharField(read_only=True, source="user.last_name")

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone', 'role', 'username', 'password')

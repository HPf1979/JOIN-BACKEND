from rest_framework import serializers
from board.models import Todo, UserProfile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    color = serializers.CharField(source='userprofile.color')

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'color']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

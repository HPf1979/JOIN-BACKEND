from rest_framework import serializers
from board.models import Todo, UserProfile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'password',
                  'last_name', 'email']
        extra_kwargs = {'username': {'required': False}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        email = validated_data.pop('email', None)
        username = email  # Benutzername automatisch mit E-Mail setzen

        user = User.objects.create_user(
            username=username, email=email, password=password, **validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['color', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        user = UserSerializer().create(validated_data=user_data)
        userprofile = UserProfile.objects.create(
            user=user, color=validated_data.pop('color', None))
        return userprofile


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

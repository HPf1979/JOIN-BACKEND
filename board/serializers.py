from rest_framework import serializers
from board.models import Todo, UserProfile
from django.contrib.auth.models import User


""" class UserSerializer(serializers.ModelSerializer):
    color = serializers.CharField(source='userprofile.color')

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'color'] """


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['color']


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'user_profile']
        extra_kwargs = {'username': {'required': False}}

    def create(self, validated_data):
        profile_data = validated_data.pop('user_profile')
        password = validated_data.pop('password', None)
        email = validated_data.get('email')
        username = email  # Benutzername automatisch mit E-Mail setzen

        # Überprüfen, ob das email-Feld bereits im user-Objekt vorhanden ist
        if 'email' in validated_data:
            del validated_data['email']

        user = User.objects.create(
            username=username, email=email, **validated_data)
        if password:
            user.set_password(password)
            user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

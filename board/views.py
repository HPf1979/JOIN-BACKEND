
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import UpdateAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from django.shortcuts import render

# Create your views here.
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from board.serializers import TodoSerializer
from board.serializers import UserSerializer, UserProfileSerializer
from board.models import Todo, UserProfile
from django.views import View
from rest_framework import status
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


class SignupView(APIView):
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
           # login(request, user)
            return Response({'success': True, 'user_id': user.id}, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class LoginUser(ObtainAuthToken):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        # Extrahiere den Vornamen des Benutzers
        first_name = user.first_name

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'first_name': first_name
        })


class TodoListView(APIView):
    allowed_methods = ['get', 'post', 'patch']

    def get(self, request):
        # Standardwert auf leeren String setzen, falls kein Status angegeben ist
        status = request.GET.get('status', '')
        if status:
            todos = Todo.objects.filter(status=status)
        else:
            todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailView(APIView):
    allowed_methods = ['patch']

    def delete(self, request, pk):
        try:
            task = Todo.objects.get(pk=pk)
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Todo.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        try:
            task = Todo.objects.get(pk=pk)
            serializer = TodoSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'Task updated successfully'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Todo.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

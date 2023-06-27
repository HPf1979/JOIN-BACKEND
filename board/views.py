from django.shortcuts import render

# Create your views here.
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from board.serializers import TodoSerializer
from board.serializers import UserSerializer
from board.models import Todo, UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from rest_framework import status
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate, login

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import UpdateAPIView


# @csrf_exempt  # Um den CSRF-Schutz vorübergehend zu deaktivieren
# def signup(request):
class SignupView(APIView):
    """ if request.method == 'POST': """
    @csrf_exempt  # Um den CSRF-Schutz vorübergehend zu deaktivieren
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        color = request.POST.get('color')

        # Überprüfe, ob bereits ein Benutzer mit der angegebenen E-Mail existiert
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Benutzer mit dieser E-Mail existiert bereits.'})

# Erstelle einen neuen Benutzer in der Datenbank
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
# Speichere das Benutzerprofil mit der Farbe
        user_profile = UserProfile.objects.create(user=user, color=color)
        # user.id abrufen und speichern
        user_id = user.id
        user.save()

 # Antworte mit einer JSON-Antwort, um den Erfolg anzuzeigen
        return JsonResponse({'success': True, 'user_id': user_id})

    # Wenn die Anfrage keine POST-Methode ist, antworte mit einem Fehler
        return JsonResponse({'error': 'Invalid request method'})


class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class Login_user(ObtainAuthToken):
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
    allowed_methods = ['get', 'post']

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
            task.title = request.data.get('title', task.title)
            task.category = request.data.get('category', task.category)
            task.description = request.data.get(
                'description', task.description)
            task.status = request.data.get('status')
            task.save()
            return Response({'success': 'Task updated successfully'})
        except Todo.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

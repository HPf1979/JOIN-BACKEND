from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from board.serializers import TodoSerializer
from board.models import Todo
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import status


# @csrf_exempt
class TodoListView(APIView):
    allowed_methods = ['get', 'post']

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

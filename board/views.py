from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View
from .models import Todo


class TodoListView(View):
    def get(self, request):
        todos = Todo.objects.all()
        allTasks = []
        for todo in todos:
            allTasks.append({
                'created_at': todo.created_at,
                'title': todo.title,
                'category': todo.category,
                'description': todo.description,
                'due_date': todo.due_date,
                'urgency': todo.urgency,
                'assigned_user': todo.assigned_user.username,
                'status': todo.status,
            })
        return JsonResponse(allTasks, safe=False)

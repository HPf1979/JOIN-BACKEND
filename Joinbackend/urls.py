"""
URL configuration for Joinbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

  
"""
from django.contrib import admin
from django.urls import path
from board.views import TodoListView, signup, login_user, UserAPIView, TodoDetailView, TodoStatusUpdateView, TodoUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todos/', TodoListView.as_view(), name='todos'),
    path('api/signup/', signup, name='signup'),
    path('api/login/', login_user.as_view(), name='api-login'),
    path('api/users/', UserAPIView.as_view(), name='user-api'),
    path('api/todos/<int:pk>/', TodoDetailView.as_view(), name='todo-delete'),
    path('api/todos/statusUpdate/<int:pk>/',
         TodoStatusUpdateView.as_view(), name='todo-status-update'),
    path('api/todos/update/<int:pk>/',
         TodoUpdateView.as_view(), name='todo-update'),
]

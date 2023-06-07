from django.contrib import admin
from .models import Todo


# class TodoAdmin (admin.ModelAdmin):
#   list_display = ('created_at', 'description', 'user', 'status')


# admin.site.register(Todo, TodoAdmin)

admin.site.register(Todo)

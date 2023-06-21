from django.contrib import admin
from .models import Todo, UserProfile

# admin.site.register(Todo, TodoAdmin)
admin.site.register(UserProfile)
admin.site.register(Todo)

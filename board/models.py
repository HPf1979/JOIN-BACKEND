from django.db import models
from django.conf import settings
from datetime import date


class Todo(models.Model):
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    due_date = models.DateField(default=date.today)
    urgency = models.CharField(max_length=500)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=500)

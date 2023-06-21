from django.db import models
from django.conf import settings
from datetime import date
import datetime
from django.contrib.auth.models import User
from jsonfield import JSONField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


class Todo(models.Model):
    created_at = models.DateField(default=date.today)
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500)
    due_date = models.DateField(default=date.today)
    urgency = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=500, null=True, blank=True)
    assignedTo = JSONField(null=True, blank=True)

    def __str__(self):
        return self.title

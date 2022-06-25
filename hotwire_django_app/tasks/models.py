from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator


class Task(models.Model):
    title = models.CharField(max_length=250,validators=[MinLengthValidator(limit_value=3)])
    due_date = models.DateField(default=timezone.now)
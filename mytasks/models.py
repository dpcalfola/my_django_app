from django.db import models


# Create your models here.

class TodayTasks(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField(null=True, blank=True)
    importance = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
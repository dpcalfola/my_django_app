from django.db import models


# Create your models here.

class TodayTasks(models.Model):
    subject = models.CharField(max_length=200)
    contents = models.TextField()
    importance = models.IntegerField()
    created_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
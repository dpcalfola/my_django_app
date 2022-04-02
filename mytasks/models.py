from django.db import models


# Create your models here.

class TodayTasks(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    importance = models.IntegerField()
    created_date = models.DateTimeField()
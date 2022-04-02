from django.contrib import admin

# Register your models here.

from .models import TodayTasks

admin.site.register(TodayTasks)
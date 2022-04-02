from django.shortcuts import render

# Create your views here.

from .models import TodayTasks


def main(request):
    """
    print TodayTasks
    """
    today_tasks_obj_list = TodayTasks.objects.order_by('created_date')
    context = {'today_tasks': today_tasks_obj_list}
    return render(request, 'mytasks/main.html', context)

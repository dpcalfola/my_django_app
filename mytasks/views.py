from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from .models import TodayTasks
from .operating_files import obj_date


# 목표 :
# main 페이지 - "오늘" 버튼 만들기
# 버튼을 누르면 오늘 날짜를 얻어와서
# /mytasks/2022-04-03 주소로 리다이렉트


def main(request):
    # TodayTasks model
    today_tasks_obj_list = TodayTasks.objects.order_by('created_date')

    # datetime obj
    today_obj = obj_date.DateObj()

    # context dictionary
    context = {
        'today_tasks': today_tasks_obj_list,
        'today_obj': today_obj
    }
    return render(request, 'mytasks/main.html', context)


def today(request, today_url):
    # TodayTasks model
    today_task_obj_list = TodayTasks.objects.order_by('created_date')

    # datetime obj
    today_obj = obj_date.DateObj()

    # context
    context = {
        'today_tasks': today_task_obj_list,
        'today_obj': today_obj
    }

    return render(request, 'mytasks/main.html', context)


def bt_test(request):
    return render(request, 'mytasks/base_template_test.html')

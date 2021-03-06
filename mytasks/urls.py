from django.urls import path
from . import views

app_name = 'mytasks'

urlpatterns = [
    path('', views.main, name='main'),
    path('<str:today_url>/', views.today, name='today'),
    path('delete/<int:task_pk>', views.delete, name='delete'),
    path('complete/<int:task_pk>/<str:is_complete>', views.complete, name='complete'),
    path('bt-test', views.bt_test, name='bt_test'),
]

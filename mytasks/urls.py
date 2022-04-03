from django.urls import path
from . import views

app_name = 'mytasks'

urlpatterns = [
    path('', views.main, name='main'),
    path('<str:today_url>/', views.today, name='today_url'),
]

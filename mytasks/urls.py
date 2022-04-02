from django.urls import path
from . import views

app_name = 'pyfo'

urlpatterns = [
    path('', views.index, name='index'),
]

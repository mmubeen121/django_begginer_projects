from . views import index, task_detail
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('<str:title>/', task_detail, name='task_detail'),
]

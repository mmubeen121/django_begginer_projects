from django.urls import path
from .views import index, topic_detail

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', topic_detail, name='topic_detail')
]

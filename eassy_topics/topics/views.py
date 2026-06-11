from django.shortcuts import render, get_object_or_404
from .models import Topics


def index(request):
    topic = Topics.objects.all()
    return render(request, 'index.html', {'topics': topic})


def topic_detail(request, pk):
    topic = get_object_or_404(Topics, pk=pk)
    return render(request, 'topic_detail.html', {'topics': topic})

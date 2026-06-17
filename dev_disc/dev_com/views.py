from django.shortcuts import render
from .models import Room
# Create your views here.


def index(request):
    rooms = Room.objects.all()
    return render(request, 'index.html', {'rooms': rooms})

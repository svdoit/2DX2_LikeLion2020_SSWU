from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import MyItem

# Create your views here.

def main(request):
    return render(request,'main.html')

def myLevel(request):
    myItems_myLevel = MyItem.objects.all()
    return render(request, 'myLevel.html', {'myItems':myItems_myLevel})



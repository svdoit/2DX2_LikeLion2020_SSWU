from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import MyItem
from .models import Tip
from .models import Item

# Create your views here.

def main(request):
    return render(request,'main.html')

def login(request):
    return render(request,'login.html')

def myLevel(request):
    myItems_myLevel = MyItem.objects.all()
    return render(request, 'myLevel.html', {'myItems':myItems_myLevel})

def tip(request):
    tips = Tip.objects.all()
    return render(request, 'tip.html', {'tips':tips})

def tipDetail(request, tip_id):
    tip_detail = get_object_or_404(Tip, pk=tip_id)
    return render(request, 'tipDetail.html', {'tip':tip_detail})

def product(request):
    return render(request, 'product.html')

def productDetail(request):
    productDetails = Item.objects.all()
    return render(request, 'productDetail.html',{'productDetails':productDetails})


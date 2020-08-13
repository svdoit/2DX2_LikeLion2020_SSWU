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

def submit_myItem(request):
    return render(request, 'submit_myItem.html')

def create(request):
    myItems = MyItem()
    myItems.myItemName = request.GET['myItemName']
    myItems.myItemStore = request.GET['myItemStore']
    myItems.myItemDate = request.GET['myItemDate']
    myItems.myItemCat = request.GET['myItemCat']
    myItems.save()
    return redirect('myLevel')

def detail_myItem(request, my_Items_id):
    myItems_detail = get_object_or_404(MyItem, pk=my_Items_id)
    return render(request, 'detail_myItem.html', {'my_Items':myItems_detail})

def update_myItem(request, my_Items_id):
    my_Items = get_object_or_404(MyItem, pk=my_Items_id)

    if request.method == "POST":
        myItemName = request.POST.get('myItemName')
        myItemStore = request.POST.get('myItemStore')
        myItemDate = request.POST.get('myItemDate')
        myItemCat = request.POST.get('myItemCat')
        my_Items.myItemName = myItemName
        my_Items.myItemStore = myItemStore
        my_Items.myItemDate = myItemDate
        my_Items.myItemCat = myItemCat
        my_Items.save()
        return redirect('detail', my_Items.id)
    return render(request, 'update_myItem.html', {'my_Items':my_Items})

def delete_myItem(request, my_Items_id):
    myItems = get_object_or_404(MyItem, pk=my_Items_id)
    myItems.delete()
    return redirect('myLevel')

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

def bathroom(request):
    return render(request, 'bathroom.html')



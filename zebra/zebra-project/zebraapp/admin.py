from django.contrib import admin
from .models import MyItem
from .models import Tip
from .models import Item
# Register your models here.
admin.site.register(MyItem)
admin.site.register(Tip)
admin.site.register(Item)
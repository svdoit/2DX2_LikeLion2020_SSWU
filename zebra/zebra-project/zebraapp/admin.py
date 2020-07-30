from django.contrib import admin
from .models import MyItem
from .models import Tip
# Register your models here.
admin.site.register(MyItem)
admin.site.register(Tip)
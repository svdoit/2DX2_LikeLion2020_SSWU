"""zebraproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from zebraapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name= "main"),
    path('login/', views.login, name ="login"),
    path('accounts/', include('allauth.urls')),
    path('myLevel', views.myLevel, name="myLevel"),
    path('tip', views.tip, name= "tip"),
    path('tip/<int:tip_id>', views.tipDetail, name="tipDetail"),
    path('product/', views.product, name="product"),
    path('productDetail/', views.productDetail, name="productDetail"),
    path('submit_myItem', views.submit_myItem, name="submit_myItem"),
    path('myLevel/create', views.create, name="create"),
    path('myLevel/<int:my_Items_id>', views.detail_myItem, name="detail"),
    path('myLevel/<int:my_Items_id>/update', views.update_myItem, name="update"),
    path('myLevel/<int:my_Items_id>/delete', views.delete_myItem, name="delete"),
    path('bathroom/', views.bathroom, name="bathroom"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

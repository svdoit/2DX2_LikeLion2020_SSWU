from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class MyItem(models.Model):
    myItemName = models.CharField(max_length=200)
    myItemStore = models.CharField(max_length=200)
    myItemDate = models.DateTimeField('date published')
    myItemCat = models.CharField(max_length=200)

    class Meta:
        ordering = ['-myItemDate']

    def __str__(self):
        return self.myItemDate.strftime("%Y.%m.%d") + "-" + self.myItemName + "-" + self.myItemStore + "-" + self.myItemCat

class Tip(models.Model):
    objects = models.Manager()
    tipTitle = models.CharField(max_length=200)
    # 추후 작성자 추가 기능 필요한지 논의
    # tipAuthor = models.ForeignKey(settings.AUTH_USER_MODEL)
    tipDate = models.DateField('date published')
    tipBody = models.TextField()
    tipImg = models.ImageField(blank=True, upload_to="images", null=True)

    def __str__(self):
        return self.tipTitle

class Item(models.Model):
    itemName = models.CharField(max_length=200, null=True)
    itemDetail = models.CharField(max_length=400, null=True)
    itemPrice = models.CharField(max_length=20, null=True)
    itemImg = ProcessedImageField(upload_to='images/', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality':80},)
    itemStore = models.CharField(max_length=50, null=True)
    itemLink = models.CharField(max_length=500, null=True)
    itemShip = models.CharField(max_length=20, null=True)
    itemCat = models.CharField(max_length=50, null=True)
    # itemLiked = models.CharField(max_length=10)

    def __str__(self):
        return self.itemName + "-" + self.itemStore


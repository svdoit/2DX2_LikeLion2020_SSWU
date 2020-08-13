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
    itemCat = models.CharField(max_length=20, null=True)

    itemName = models.CharField(max_length=200, null=True)
    itemDetail = models.CharField(max_length=400, null=True)
    itemPrice = models.CharField(max_length=20, null=True)
    itemImg = ProcessedImageField(upload_to='images/', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality':80}, null=True)
    itemStore = models.CharField(max_length=50, null=True)
    itemLink = models.CharField(max_length=500, null=True)
    itemShip = models.CharField(max_length=20, null=True)
    
    itemName1 = models.CharField(max_length=200, null=True, blank=True)
    itemDetail1 = models.CharField(max_length=400, null=True, blank=True)
    itemPrice1 = models.CharField(max_length=20, null=True, blank=True)
    itemImg1 = ProcessedImageField(upload_to='images/', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality':80}, null=True, blank=True)
    itemStore1 = models.CharField(max_length=50, null=True, blank=True)
    itemLink1 = models.CharField(max_length=500, null=True, blank=True)
    itemShip1 = models.CharField(max_length=20, null=True, blank=True)

    itemName2 = models.CharField(max_length=200, null=True, blank=True)
    itemDetail2 = models.CharField(max_length=400, null=True, blank=True)
    itemPrice2 = models.CharField(max_length=20, null=True, blank=True)
    itemImg2 = ProcessedImageField(upload_to='images/', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality':80}, null=True, blank=True)
    itemStore2 = models.CharField(max_length=50, null=True, blank=True)
    itemLink2 = models.CharField(max_length=500, null=True, blank=True)
    itemShip2 = models.CharField(max_length=20, null=True, blank=True)

    itemName3 = models.CharField(max_length=200, null=True, blank=True)
    itemDetail3 = models.CharField(max_length=400, null=True, blank=True)
    itemPrice3 = models.CharField(max_length=20, null=True, blank=True)
    itemImg3 = ProcessedImageField(upload_to='images/', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality':80}, null=True, blank=True)
    itemStore3 = models.CharField(max_length=50, null=True, blank=True)
    itemLink3 = models.CharField(max_length=500, null=True, blank=True)
    itemShip3 = models.CharField(max_length=20, null=True, blank=True)

    itemName4 = models.CharField(max_length=200, null=True, blank=True)
    itemDetail4 = models.CharField(max_length=400, null=True, blank=True)
    itemPrice4 = models.CharField(max_length=20, null=True, blank=True)
    itemImg4 = ProcessedImageField(upload_to='images/', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality':80}, null=True, blank=True)
    itemStore4 = models.CharField(max_length=50, null=True, blank=True)
    itemLink4 = models.CharField(max_length=500, null=True, blank=True)
    itemShip4 = models.CharField(max_length=20, null=True, blank=True)

    itemName5 = models.CharField(max_length=200, null=True, blank=True)
    itemDetail5 = models.CharField(max_length=400, null=True, blank=True)
    itemPrice5 = models.CharField(max_length=20, null=True, blank=True)
    itemImg5 = ProcessedImageField(upload_to='images/', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality':80}, null=True, blank=True)
    itemStore5 = models.CharField(max_length=50, null=True, blank=True)
    itemLink5 = models.CharField(max_length=500, null=True, blank=True)
    itemShip5 = models.CharField(max_length=20, null=True, blank=True)


    # CATEGORY = (
    #     ('0', 'Bathroom'),
    #     ('1', 'Kitchen'),
    #     ('2', 'Living'),
    #     ('3', 'Office'),
    # )
    # itemCat = models.CharField(max_length=50, null=True, choices=CATEGORY)
    # itemLiked = models.CharField(max_length=10)

    def __str__(self):
        return self.itemCat


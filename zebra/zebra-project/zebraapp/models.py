from django.db import models

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
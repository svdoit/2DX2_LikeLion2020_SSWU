# Generated by Django 3.0.8 on 2020-08-06 05:59

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('zebraapp', '0003_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='itemCat',
            new_name='itemStore1',
        ),
        migrations.AddField(
            model_name='item',
            name='itemDetail1',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='itemImg1',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='item',
            name='itemLink1',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='itemName1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='itemPrice1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='itemShip1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='itemImg',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='images/'),
        ),
    ]

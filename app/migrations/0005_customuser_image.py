# Generated by Django 4.2 on 2023-04-11 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_order_ordershistory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='image.svg', upload_to='photos/%y/%m/%d'),
        ),
    ]

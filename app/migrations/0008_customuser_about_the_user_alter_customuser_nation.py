# Generated by Django 4.2 on 2023-04-11 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_customuser_nation'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about_the_user',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='nation',
            field=models.CharField(default='', max_length=100),
        ),
    ]

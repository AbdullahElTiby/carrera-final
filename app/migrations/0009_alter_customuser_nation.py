# Generated by Django 4.2 on 2023-04-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_customuser_about_the_user_alter_customuser_nation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='nation',
            field=models.CharField(default='', max_length=100),
        ),
    ]

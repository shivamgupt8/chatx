# Generated by Django 2.2.3 on 2019-08-08 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190808_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]

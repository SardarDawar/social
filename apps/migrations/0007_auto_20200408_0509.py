# Generated by Django 2.2 on 2020-04-08 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_instaimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instaimg',
            name='img',
            field=models.ImageField(null=True, upload_to='temp', verbose_name='Image for Instagram'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-23 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_widgetuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widgetuser',
            name='profile_pic',
            field=models.FileField(blank=True, null=True, upload_to='media/homepage'),
        ),
    ]
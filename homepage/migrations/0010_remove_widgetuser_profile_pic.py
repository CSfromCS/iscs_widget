# Generated by Django 4.0.4 on 2022-09-16 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_remove_widgetuser_department_delete_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='widgetuser',
            name='profile_pic',
        ),
    ]

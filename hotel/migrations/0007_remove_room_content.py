# Generated by Django 3.2.19 on 2023-06-25 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_auto_20230625_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='content',
        ),
    ]
# Generated by Django 3.2.19 on 2023-06-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20230610_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='content',
            field=models.TextField(),
        ),
    ]

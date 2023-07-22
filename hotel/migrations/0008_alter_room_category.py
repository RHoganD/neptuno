# Generated by Django 3.2.19 on 2023-06-28 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_remove_room_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_list', to='hotel.category'),
        ),
    ]
# Generated by Django 3.0 on 2022-04-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0002_alter_hotel_hotel_main_img_alter_hotel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 3.2.8 on 2022-05-22 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayfalar', '0002_auto_20220522_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film_slider',
            name='slider_resim',
            field=models.FileField(upload_to='filmler/slider', verbose_name='Slider Resmi'),
        ),
    ]

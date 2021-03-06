# Generated by Django 3.2.8 on 2022-05-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayfalar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film_slider',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Aktif Slider'),
        ),
        migrations.AlterField(
            model_name='film_slider',
            name='slider_etiket',
            field=models.CharField(blank=True, max_length=50, verbose_name='Slider Etiketi'),
        ),
    ]

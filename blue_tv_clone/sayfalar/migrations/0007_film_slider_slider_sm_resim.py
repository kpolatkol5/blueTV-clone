# Generated by Django 3.2.8 on 2022-05-23 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayfalar', '0006_delete_deneme'),
    ]

    operations = [
        migrations.AddField(
            model_name='film_slider',
            name='slider_sm_resim',
            field=models.FileField(blank=True, default=False, upload_to='filmler/slider', verbose_name='Slider Küçük Resim'),
        ),
    ]
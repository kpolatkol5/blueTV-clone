# Generated by Django 3.2.8 on 2022-06-04 11:25

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sayfalar', '0012_auto_20220525_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiziKategorileri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori_adi', models.CharField(max_length=50, verbose_name='Dizi Kategorileri')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='Aktif Kategori')),
                ('is_pages', models.BooleanField(default=False, help_text='Kategori aktif olarak ulaşılabilir ancak film sayfasında gösterilmez', verbose_name='Sayfada Göster')),
            ],
            options={
                'verbose_name': 'Dizi Kategorisi',
                'verbose_name_plural': 'Dizi Kategorileri',
                'db_table': 'dizi_kategorileri',
            },
        ),
        migrations.CreateModel(
            name='Diziler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dizi_adi', models.CharField(max_length=50, verbose_name='Dizi Adı')),
                ('imdb_puani', models.FloatField(verbose_name='Dizi İMDB puanı')),
                ('dizi_aciklama', ckeditor.fields.RichTextField(verbose_name='Açıklama')),
                ('dizi_resmi', models.FileField(upload_to='sayfalar/diziler')),
                ('is_active', models.BooleanField(default=False, verbose_name='Aktif Dizi')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('dizi_kucuk_resmi', models.FileField(upload_to='sayfalar/diziler/kucuk_resimler', verbose_name='Dizi Küçük Resim')),
                ('dizi_kategorileri', models.ManyToManyField(related_name='diziler', to='sayfalar.DiziKategorileri')),
                ('dublaj', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sayfalar.dublaj', verbose_name='Dublaj Seç')),
                ('oyuncular', models.ManyToManyField(related_name='oyuncuDizi', to='sayfalar.Oyuncular')),
                ('yonetmen', models.ManyToManyField(related_name='yonetmenDizi', to='sayfalar.Yonetmenler')),
            ],
            options={
                'verbose_name': 'Dizi',
                'verbose_name_plural': 'Diziler',
                'db_table': 'diziler',
            },
        ),
        migrations.CreateModel(
            name='DiziSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_resim', models.FileField(upload_to='diziler/slider', verbose_name='Slider Resmi')),
                ('slider_aciklama', ckeditor.fields.RichTextField(verbose_name='Slider Açıklama')),
                ('slider_etiket', models.CharField(blank=True, max_length=50, verbose_name='Slider Etiketi')),
                ('is_active', models.BooleanField(default=False, verbose_name='Aktif Slider')),
                ('slider_sm_resim', models.FileField(blank=True, upload_to='diziler/slider', verbose_name='Slider Küçük Resim')),
                ('slider_dizi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sayfalar.diziler')),
            ],
            options={
                'verbose_name': 'Dizi Slider',
                'verbose_name_plural': 'Dizi Slider',
                'db_table': 'dizi-slider',
            },
        ),
    ]

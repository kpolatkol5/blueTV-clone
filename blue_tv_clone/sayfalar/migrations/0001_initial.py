# Generated by Django 3.2.8 on 2022-05-22 18:40

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dublaj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dublaj_adi', models.CharField(max_length=20, verbose_name='dublaj adı')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Dublaj',
                'verbose_name_plural': 'Dublajlar',
                'db_table': 'dublaj',
            },
        ),
        migrations.CreateModel(
            name='Film_kategorileri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori_adi', models.CharField(max_length=50, verbose_name='Film Kategorileri')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Film Kategorisi',
                'verbose_name_plural': 'Film Kategorileri',
                'db_table': 'film_kategorileri',
            },
        ),
        migrations.CreateModel(
            name='Oyuncular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oyuncu_adi', models.CharField(max_length=50, verbose_name='Oyuncu Adı')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Oyuncu',
                'verbose_name_plural': 'Oyuncular',
                'db_table': 'oyuncular',
            },
        ),
        migrations.CreateModel(
            name='Yonetmenler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yonetmen_adi', models.CharField(max_length=50, verbose_name='Yönetmen')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Yönetmen',
                'verbose_name_plural': 'Yönetmenler',
                'db_table': 'yonetmen',
            },
        ),
        migrations.CreateModel(
            name='Filmler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_adi', models.CharField(max_length=50, verbose_name='Fİlm Adı')),
                ('imdb_puani', models.FloatField(verbose_name='Filmin İMDB puanı')),
                ('film_aciklama', ckeditor.fields.RichTextField()),
                ('film_cikis_tarihi', models.DateTimeField()),
                ('film_resmi', models.ImageField(upload_to='sayfalar/filmler')),
                ('is_active', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('dublaj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sayfalar.dublaj', verbose_name='Dublaj Seç')),
                ('film_kategoriler', models.ManyToManyField(related_name='film_kategorileri', to='sayfalar.Film_kategorileri')),
                ('oyuncular', models.ManyToManyField(related_name='oyuncular', to='sayfalar.Oyuncular')),
                ('yonetmen', models.ManyToManyField(related_name='yonetmen', to='sayfalar.Yonetmenler')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filmler',
                'db_table': 'filmler',
            },
        ),
        migrations.CreateModel(
            name='Film_slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_resim', models.ImageField(upload_to='filmler/slider', verbose_name='Slider Resmi')),
                ('slider_aciklama', ckeditor.fields.RichTextField()),
                ('slider_etiket', models.CharField(max_length=50, verbose_name='Slider Etiketi')),
                ('slider_film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sayfalar.filmler')),
            ],
        ),
    ]
# Generated by Django 3.2.8 on 2022-05-25 12:31

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sayfalar', '0010_alter_filmler_film_kategoriler'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmkategorileri',
            name='is_pages',
            field=models.BooleanField(default=False, help_text='Kategori aktif olarak ulaşılabilir ancak film sayfasında gösterilmez', verbose_name='Sayfada Göster'),
        ),
        migrations.AddField(
            model_name='filmler',
            name='film_kucuk_resmi',
            field=models.FileField(blank=True, null=True, upload_to='sayfalar/filmler/kucuk_resimler', verbose_name='Film Küçük Resim'),
        ),
        migrations.AlterField(
            model_name='filmkategorileri',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Aktif Kategori'),
        ),
        migrations.AlterField(
            model_name='filmler',
            name='dublaj',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sayfalar.dublaj', verbose_name='Dublaj Seç'),
        ),
        migrations.AlterField(
            model_name='filmler',
            name='film_aciklama',
            field=ckeditor.fields.RichTextField(verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='filmler',
            name='film_cikis_tarihi',
            field=models.DateField(verbose_name='Filmin Çıkış Tarihi'),
        ),
        migrations.AlterField(
            model_name='filmler',
            name='oyuncular',
            field=models.ManyToManyField(related_name='Oyuncular', to='sayfalar.Oyuncular'),
        ),
        migrations.AlterField(
            model_name='filmler',
            name='yonetmen',
            field=models.ManyToManyField(related_name='Yönetmen', to='sayfalar.Yonetmenler'),
        ),
    ]

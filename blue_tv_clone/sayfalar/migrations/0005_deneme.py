# Generated by Django 3.2.8 on 2022-05-22 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayfalar', '0004_alter_filmler_film_resmi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deneme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deneme_text', models.CharField(max_length=30)),
            ],
        ),
    ]
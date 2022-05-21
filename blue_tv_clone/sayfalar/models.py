from django.db import models

# Create your models here.

class Dublaj(models.Model):
    dublaj_adi  =   models.CharField(verbose_name="dublaj adı" , max_length=20)



class filmler(models.Model):
    film_adi    =   models.CharField(verbose_name   = "Fİlm Adı", max_length=50)
    imdb_puani  =   models.FloatField(verbose_name  = "Filmin İMDB puanı")
    dublaj      =   models.ForeignKey(Dublaj, on_delete = models.CASCADE)
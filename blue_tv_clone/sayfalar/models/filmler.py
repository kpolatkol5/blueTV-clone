from django.db import models
from sayfalar.models.oyuncular import Oyuncular
from sayfalar.models.yonetmenler import Yonetmenler
from sayfalar.models.film_kategorileri import FilmKategorileri
from sayfalar.models.dublaj import Dublaj

from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Filmler(models.Model):
    film_adi            =   models.CharField(verbose_name   = "Film Adı", max_length = 50)
    imdb_puani          =   models.FloatField(verbose_name  = "Filmin İMDB puanı")
    dublaj              =   models.ForeignKey(Dublaj,verbose_name = "Dublaj Seç", blank = True, on_delete = models.CASCADE)
    film_kategoriler    =   models.ManyToManyField(FilmKategorileri , related_name = "filmler")
    yonetmen            =   models.ManyToManyField(Yonetmenler , related_name = "Yönetmen")
    film_aciklama       =   RichTextField(verbose_name = "Açıklama")
    oyuncular           =   models.ManyToManyField(Oyuncular , related_name = "Oyuncular")
    film_resmi          =   models.FileField(upload_to = "sayfalar/filmler")
    is_active           =   models.BooleanField(default = False , verbose_name="Aktif Film")
    slug                =   models.SlugField(null = False, blank = True, unique = True, db_index = True, editable = False)
    film_kucuk_resmi    =   models.FileField(upload_to = "sayfalar/filmler/kucuk_resimler" ,  null=True , blank=True ,verbose_name = "Film Küçük Resim")

    def __str__(self):
        return self.film_adi

    def save(self , *args , **kwargs):
        self.slug=slugify(self.film_adi)
        super().save(*args,**kwargs)


    class Meta:
        db_table            =   "filmler"
        verbose_name        =   "Film"
        verbose_name_plural =   "Filmler"
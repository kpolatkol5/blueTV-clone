from django.db import models
from sayfalar.models.oyuncular import Oyuncular
from sayfalar.models.yonetmenler import Yonetmenler
from sayfalar.models.film_kategorileri import Film_kategorileri
from sayfalar.models.dublaj import Dublaj

from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Filmler(models.Model):
    film_adi            =   models.CharField(verbose_name   = "Fİlm Adı", max_length=50)
    imdb_puani          =   models.FloatField(verbose_name  = "Filmin İMDB puanı")
    dublaj              =   models.ForeignKey(Dublaj,verbose_name="Dublaj Seç", on_delete = models.CASCADE)
    film_kategoriler    =   models.ManyToManyField(Film_kategorileri , related_name="film_kategorileri")
    yonetmen            =   models.ManyToManyField(Yonetmenler , related_name="yonetmen")
    film_aciklama       =   RichTextField()
    film_cikis_tarihi   =   models.DateTimeField()
    oyuncular           =   models.ManyToManyField(Oyuncular , related_name="oyuncular")
    film_resmi          =   models.FileField(upload_to="sayfalar/filmler")
    is_active           =   models.BooleanField(default=False)
    slug                =   models.SlugField(null=False ,blank=True,unique=True, db_index=True,editable=False )
        

    def __str__(self):
        return self.film_adi

    def save(self , *args , **kwargs):
        self.slug=slugify(self.film_adi)
        super().save(*args,**kwargs)


    class Meta:
        db_table            =   "filmler"
        verbose_name        =   "Film"
        verbose_name_plural =   "Filmler"
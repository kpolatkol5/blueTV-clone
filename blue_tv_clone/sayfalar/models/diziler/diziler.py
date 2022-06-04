from django.db import models
from sayfalar.models.filmler.oyuncular import Oyuncular
from sayfalar.models.filmler.yonetmenler import Yonetmenler
from sayfalar.models.filmler.dublaj import Dublaj
from sayfalar.models.diziler.dizi_kategorileri import DiziKategorileri
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Diziler(models.Model):
    dizi_adi            =   models.CharField(verbose_name   = "Dizi Adı", max_length = 50)
    imdb_puani          =   models.FloatField(verbose_name  = "Dizi İMDB puanı")
    dublaj              =   models.ForeignKey(Dublaj    ,   verbose_name = "Dublaj Seç", blank = True, on_delete = models.CASCADE)
    dizi_kategorileri    =   models.ManyToManyField(DiziKategorileri , related_name = "diziler")
    yonetmen            =   models.ManyToManyField(Yonetmenler , related_name = "yonetmenDizi")
    dizi_aciklama       =   RichTextField(verbose_name = "Açıklama")
    oyuncular           =   models.ManyToManyField(Oyuncular , related_name = "oyuncuDizi")
    dizi_resmi          =   models.FileField(upload_to = "sayfalar/diziler")
    is_active           =   models.BooleanField(default = False , verbose_name="Aktif Dizi")
    slug                =   models.SlugField(null = False, blank = True, unique = True, db_index = True, editable = False)
    dizi_kucuk_resmi    =   models.FileField(upload_to = "sayfalar/diziler/kucuk_resimler" ,verbose_name = "Dizi Küçük Resim")

    def __str__(self):
        return self.dizi_adi

    def save(self , *args , **kwargs):
        self.slug=slugify(self.dizi_adi)
        super().save(*args,**kwargs)


    class Meta:
        db_table            =   "diziler"
        verbose_name        =   "Dizi"
        verbose_name_plural =   "Diziler"
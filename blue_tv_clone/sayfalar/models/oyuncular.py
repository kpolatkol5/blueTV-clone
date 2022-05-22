from django.db import models
from django.utils.text import slugify

class Oyuncular(models.Model):

    oyuncu_adi  =   models.CharField(verbose_name="Oyuncu Adı", max_length=50)
    slug        =   models.SlugField(null=False ,blank=True,unique=True, db_index=True,editable=False )
    is_active   =   models.BooleanField(default=False)
    
    def __str__(self):
        return self.oyuncu_adi

    def save(self , *args , **kwargs):
        self.slug=slugify(self.oyuncu_adi)
        super().save(*args,**kwargs)

    class Meta:
        db_table            =   "oyuncular"
        verbose_name        =   "Oyuncu"
        verbose_name_plural =   "Oyuncular"
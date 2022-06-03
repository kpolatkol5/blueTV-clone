from django.db import models
from django.utils.text import slugify



class Dublaj(models.Model):
    dublaj_adi      =   models.CharField(verbose_name="dublaj adı" , max_length=20)
    slug            =   models.SlugField(null = False , blank = True, unique = True, db_index = True, editable = False )
    is_active       =   models.BooleanField(default=False)
    
    def __str__(self):
        return self.dublaj_adi

    def save(self , *args , **kwargs):
        self.slug=slugify(self.dublaj_adi)
        super().save(*args,**kwargs)

    class Meta:
        db_table            =   "dublaj"
        verbose_name        =   "Dublaj"
        verbose_name_plural =   "Dublajlar"
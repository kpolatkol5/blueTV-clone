from django.db import models
from django.utils.text import slugify

class Yonetmenler(models.Model):
    yonetmen_adi    =   models.CharField(max_length=50 , verbose_name="Yönetmen")
    slug            =   models.SlugField(null=False ,blank=True,unique=True, db_index=True,editable=False )
    is_active       =   models.BooleanField(default=False)
    
    def __str__(self):
        return self.yonetmen_adi

    def save(self , *args , **kwargs):
        self.slug=slugify(self.yonetmen_adi)
        super().save(*args,**kwargs)

    class Meta:
        db_table            =   "yonetmen"
        verbose_name        =   "Yönetmen"
        verbose_name_plural =   "Yönetmenler"


from django.db import models
from django.utils.text import slugify


class DiziKategorileri(models.Model):
    kategori_adi    =   models.CharField(max_length = 50 , verbose_name = "Dizi Kategorileri")
    slug            =   models.SlugField(null = False, blank = True, unique = True, db_index = True, editable = False )
    is_active       =   models.BooleanField(default = False , verbose_name="Aktif Kategori")
    is_pages        =   models.BooleanField(default=False , verbose_name="Sayfada Göster" , help_text="Kategori aktif olarak ulaşılabilir ancak film sayfasında gösterilmez")
    
    def __str__(self):
        return self.kategori_adi

    def save(self , *args , **kwargs):
        self.slug=slugify(self.kategori_adi)
        super().save(*args,**kwargs)

    class Meta:
        db_table            =   "dizi_kategorileri"
        verbose_name        =   "Dizi Kategorisi"
        verbose_name_plural =   "Dizi Kategorileri"
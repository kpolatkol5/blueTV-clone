from django.db import models
from sayfalar.models.diziler.diziler import Diziler
from ckeditor.fields import RichTextField


class DiziSlider(models.Model):
    slider_resim    =   models.FileField(upload_to = "diziler/slider" , verbose_name = "Slider Resmi")
    slider_aciklama =   RichTextField(verbose_name="Slider Açıklama")
    slider_etiket   =   models.CharField(max_length = 50 , verbose_name = "Slider Etiketi" , blank=True)
    slider_dizi     =   models.ForeignKey(Diziler, on_delete = models.CASCADE)
    is_active       =   models.BooleanField(default = False , verbose_name = "Aktif Slider")
    slider_sm_resim =   models.FileField(upload_to = "diziler/slider" , verbose_name = "Slider Küçük Resim" , blank = True)
    
    
    def __str__(self):
        return self.slider_dizi.dizi_adi


    class Meta:
        db_table            =   "dizi-slider"
        verbose_name        =   "Dizi Slider"
        verbose_name_plural =   "Dizi Slider"





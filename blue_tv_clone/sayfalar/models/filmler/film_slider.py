from django.db import models
from sayfalar.models.filmler.filmler import Filmler
from ckeditor.fields import RichTextField


class FilmSlider(models.Model):
    slider_resim    =   models.FileField(upload_to = "filmler/slider" , verbose_name = "Slider Resmi")
    slider_aciklama =   RichTextField()
    slider_etiket   =   models.CharField(max_length = 50 , verbose_name = "Slider Etiketi" , blank=True)
    slider_film     =   models.ForeignKey(Filmler, on_delete = models.CASCADE)
    is_active       =   models.BooleanField(default = False , verbose_name = "Aktif Slider")
    slider_sm_resim =   models.FileField(upload_to = "filmler/slider" , verbose_name = "Slider Küçük Resim" , blank = True)
    
    
    def __str__(self):
        return self.slider_film.film_adi

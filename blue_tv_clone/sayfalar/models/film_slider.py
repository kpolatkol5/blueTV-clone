from django.db import models
from sayfalar.models.filmler import Filmler
from ckeditor.fields import RichTextField


class Film_slider(models.Model):
    slider_resim    =   models.FileField(upload_to="filmler/slider" , verbose_name="Slider Resmi")
    slider_aciklama =   RichTextField()
    slider_etiket   =   models.CharField(max_length=50 , verbose_name="Slider Etiketi" , blank=True)
    slider_film     =   models.ForeignKey(Filmler, on_delete=models.CASCADE)
    is_active       =   models.BooleanField(default=False , verbose_name="Aktif Slider")

    def __str__(self):
        return self.slider_film.film_adi

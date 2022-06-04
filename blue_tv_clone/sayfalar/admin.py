from django.contrib import admin

#  filmler model dosyları import
from sayfalar.models.filmler.dublaj import Dublaj
from sayfalar.models.filmler.film_kategorileri import FilmKategorileri
from sayfalar.models.filmler.filmler import Filmler
from sayfalar.models.filmler.oyuncular import Oyuncular
from sayfalar.models.filmler.yonetmenler import Yonetmenler
from sayfalar.models.filmler.film_slider import FilmSlider


#  Diziler model dosyları import
from sayfalar.models.diziler.dizi_kategorileri import DiziKategorileri
from sayfalar.models.diziler.dizi_slider import DiziSlider
from sayfalar.models.diziler.diziler import Diziler


#  Jet admin panel import
from jet.admin import CompactInline


class Film_admin(admin.ModelAdmin):
    list_display=("film_adi","dublaj","is_active",)




admin.site.register(Dublaj)
admin.site.register(FilmKategorileri)
admin.site.register(FilmSlider)
admin.site.register(Filmler , Film_admin)
admin.site.register(Oyuncular)
admin.site.register(Yonetmenler)

# diziler

admin.site.register(DiziKategorileri)
admin.site.register(DiziSlider)
admin.site.register(Diziler)





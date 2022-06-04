from django.contrib import admin
from sayfalar.models.filmler.dublaj import Dublaj
from sayfalar.models.filmler.film_kategorileri import FilmKategorileri
from sayfalar.models.filmler.filmler import Filmler
from sayfalar.models.filmler.oyuncular import Oyuncular
from sayfalar.models.filmler.yonetmenler import Yonetmenler
from sayfalar.models.filmler.film_slider import FilmSlider
from jet.admin import CompactInline


class Film_admin(admin.ModelAdmin):
    list_display=("film_adi","dublaj","is_active",)




admin.site.register(Dublaj)
admin.site.register(FilmKategorileri)
admin.site.register(FilmSlider)
admin.site.register(Filmler , Film_admin)
admin.site.register(Oyuncular)
admin.site.register(Yonetmenler)




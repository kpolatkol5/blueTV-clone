from django.contrib import admin
from sayfalar.models.dublaj import Dublaj
from sayfalar.models.film_kategorileri import FilmKategorileri
from sayfalar.models.filmler import Filmler
from sayfalar.models.oyuncular import Oyuncular
from sayfalar.models.yonetmenler import Yonetmenler
from sayfalar.models.film_slider import FilmSlider







admin.site.register(Dublaj)
admin.site.register(FilmKategorileri)
admin.site.register(Filmler)
admin.site.register(Oyuncular)
admin.site.register(Yonetmenler)
admin.site.register(FilmSlider)





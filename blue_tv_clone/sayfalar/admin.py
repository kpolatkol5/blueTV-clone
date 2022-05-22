from django.contrib import admin
from sayfalar.models.dublaj import Dublaj
from sayfalar.models.film_kategorileri import Film_kategorileri
from sayfalar.models.filmler import Filmler
from sayfalar.models.oyuncular import Oyuncular
from sayfalar.models.yonetmenler import Yonetmenler
from sayfalar.models.film_slider import Film_slider







admin.site.register(Dublaj)
admin.site.register(Film_kategorileri)
admin.site.register(Filmler)
admin.site.register(Oyuncular)
admin.site.register(Yonetmenler)
admin.site.register(Film_slider)





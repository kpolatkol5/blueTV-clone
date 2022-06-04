from django.urls import path
from sayfalar.views.anasayfa_views.anasayfa import anasayfa
from sayfalar.views.film_views.filmler import filmler
from sayfalar.views.dizi_views.diziler import diziler
from sayfalar.views.kategori_views.filmKategoriDetay import film_kategori_detay



urlpatterns = [
    path("" , anasayfa , name="anasayfa"),
    path("filmler/" , filmler , name="filmler"),
    path("diziler",diziler, name="diziler"),
    path("kategori/<slug:slug>",film_kategori_detay, name="film-kategori")
]

from django.urls import path
from sayfalar.views.anasayfa_views.anasayfa import anasayfa
from sayfalar.views.film_views.filmler import filmler
from sayfalar.views.kategori_views.filmKategoriDetay import film_kategori_detay



urlpatterns = [
    path("" , anasayfa , name="anasayfa"),
    path("film/" , filmler , name="filmler"),
    path("kategori/<slug:slug>",film_kategori_detay, name="film-kategori")
]

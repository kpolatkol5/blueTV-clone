from django.urls import path
from sayfalar.views.anasayfa_views.anasayfa import anasayfa
from sayfalar.views.film_views.filmler import filmler
from sayfalar.views.film_views.kategoriler import kategoriler



urlpatterns = [
    path("" , anasayfa , name="anasayfa"),
    path("film/" , filmler , name="filmler"),
    path("kategori/<slug:slug>",kategoriler, name="film-kategori")
]

from django.shortcuts import render
from sayfalar.models.filmler.film_kategorileri import FilmKategorileri


def film_kategori_detay(request,slug):

    context={
        "kategori":FilmKategorileri.objects.get(slug=slug),
        "kategorideki_filmler":FilmKategorileri.objects.get(slug=slug).filmler.filter(is_active=True)
    }

    return render(request,"sayfalar/kategori/film_kategori_detay.html" , context)
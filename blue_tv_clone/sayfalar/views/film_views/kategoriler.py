from django.shortcuts import render
from sayfalar.models.filmler.film_kategorileri import FilmKategorileri


def kategoriler(request,slug):

    context={
        "kategori":FilmKategorileri.objects.get(slug=slug),
        "kategorideki_filmler":FilmKategorileri.objects.get(slug=slug).filmler.filter(is_active=True)
    }

    return render(request,"sayfalar/filmler/film_kategori_detay.html" , context)
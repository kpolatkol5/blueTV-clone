from django.shortcuts import render
from sayfalar.models.filmler import Filmler
from sayfalar.models.film_slider import Film_slider
from sayfalar.models.film_kategorileri import Film_kategorileri


def filmler(request):

    film_slider =   Film_slider.objects.filter(is_active="True")
    film_kategorileri   =   Film_kategorileri.objects.filter(is_active="True")

    context={

        "film_slider": film_slider,
        "film_kategorileri":film_kategorileri,
    }
    return render(request, "sayfalar/filmler/film.html" ,context)
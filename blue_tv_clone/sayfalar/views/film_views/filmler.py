from django.shortcuts import render
from sayfalar.models.filmler import Filmler
from sayfalar.models.film_slider import Film_slider


def filmler(request):

    film_slider =   Film_slider.objects.filter(is_active="True")

    context={

        "film_slider": film_slider,
        "deneme":"deeneme",
    }
    return render(request, "sayfalar/filmler/film.html" ,context)
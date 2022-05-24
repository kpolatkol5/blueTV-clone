from django.shortcuts import render
from sayfalar.models.filmler import Filmler
from sayfalar.models.film_slider import FilmSlider
from sayfalar.models.film_kategorileri import FilmKategorileri


def filmler(request):
    def categori_in_filmler(kategori):

        """
             Bu fonksiyon çoka çok ilişkili olan kategorilerin geriye dönük sorgularında filmleri kategorilere göre almak için kullanıyorum. Tek tek get() metodu kullanmak istemedim. Katagorileri tek tek alır , kategori adı ve  kategoriye ait olan filmleri bir listeye atar.
        """
        result=[]
        for i in kategori:
            filmler =   FilmKategorileri.objects.get(kategori_adi = i.kategori_adi).filmler.filter(is_active = "True")
            result.append([i.kategori_adi,filmler])

        return result


    film_slider             =   FilmSlider.objects.filter(is_active="True")
    film_kategorileri       =   FilmKategorileri.objects.filter(is_active="True")
    kategorideki_filmler    =   categori_in_filmler(kategori=film_kategorileri)
    
    context={

        "film_slider"           :   film_slider,
        "film_kategorileri"     :   film_kategorileri,
        "kategorideki_filmler"  :   kategorideki_filmler,

    }
    return render(request, "sayfalar/filmler/film.html" ,context)
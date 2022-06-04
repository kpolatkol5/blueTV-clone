from django.shortcuts import render
from sayfalar.models.diziler.diziler import Diziler
from sayfalar.models.diziler.dizi_slider import DiziSlider
from sayfalar.models.diziler.dizi_kategorileri import DiziKategorileri


def diziler(request):

    def categori_in_diziler(kategori):
        """ 
        Bu fonksiyon çoka çok ilişkili olan kategorilerin geriye dönük sorgularında filmleri
        kategorilere göre almak için kullanıyorum. Tek tek get() metodu kullanmak istemedim.
        Katagorileri tek tek alır , kategori adı ve  kategoriye ait olan filmleri bir listeye atar.
        """

        result  =   []

        for i in kategori:
            diziler    =   DiziKategorileri.objects.get(kategori_adi=i.kategori_adi).diziler.filter(is_active=True)

            result.append({"kategori_adi":i , "kategorinin_dizileri":diziler,})

        return result

    dizi_slider             =   DiziSlider.objects.filter(is_active=True)
    dizi_kategorileri       =   DiziKategorileri.objects.filter(is_active=True , is_pages=True)
    kategorideki_diziler    = categori_in_diziler(kategori=dizi_kategorileri)  


    context={
        "dizi_slider":dizi_slider,
        "dizi_kategorileri":dizi_kategorileri,
        "kategorideki_diziler":kategorideki_diziler,
    }

    return render(request, "sayfalar/diziler/diziler.html",context)
from django import template
from sayfalar.models.filmler.film_kategorileri import FilmKategorileri


register    =   template.Library()

@register.simple_tag
def kategori_list():
    pass
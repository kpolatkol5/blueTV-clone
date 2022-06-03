from django import template
from sayfalar.models.film_kategorileri import FilmKategorileri


register    =   template.Library()

@register.simple_tag
def kategori_list():
    pass

from os import link
from unicodedata import category
from .models import Category


def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

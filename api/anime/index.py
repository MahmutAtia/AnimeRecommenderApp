from algoliasearch_django.decorators import register
from algoliasearch_django import AlgoliaIndex

from .models import Anime



@register(Anime)
class AnimeIndex(AlgoliaIndex):
    fields = ('title', 'synopsis')
    #tags = 'genre'

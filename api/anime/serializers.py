from rest_framework.serializers import ModelSerializer
from .models import Anime


class AnimeSerializer(ModelSerializer):
    class Meta:
        model = Anime
        fields= ['title', 'synopsis', 'genre', 'img_url', 'aired', 'episodes',
       'episodes', 'ranked', 'score']
            
from django.shortcuts import render, HttpResponse,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.viewsets import ModelViewSet
from .models import Genre,Anime
from .serializers import AnimeSerializer
import pandas as pd 
import pickle
import os
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Create your views here.

class AnimeApi(ModelViewSet):
    serializer_class = AnimeSerializer
    queryset = Anime.objects.all()[:100]

    def retrieve(self, request,pk=None):
        queryset = Anime.objects.all()
        anime = get_object_or_404(queryset,pk=pk)
        print(anime)
        serializer_class = AnimeSerializer(anime)
        return Response(serializer_class.data)
    
# class GenreApi(ModelViewSet):
#     serializer_class = AnimeSerializer
    

#     def get_queryset(self):
#         queryset = Anime.objects.all()
#         pk = self.request.query_params.get('pk')
#         queryset = queryset.filter(Genre=pk)
#         return queryset

@api_view(["GET"])   
def get_genre(request,pk):
    queryset = Anime.objects.all()
    objects = queryset.filter(genre=pk)
    serializer = AnimeSerializer(objects, many = True)
            
    return Response(serializer.data[:100])



@api_view(["GET"])   
def recommend(request,title):
    path = Path(__file__).parent/Path("model.pkl")

    with open(path, "rb" ) as f:
        model = pickle.load(f)
    print( model)

            
    return HttpResponse(f"hello world {title}")



# @api_view(["GET"])
# def get(request):
#     objects = Anime.objects.all()
#     serializer = AnimeSerializer(objects[:10], many = True)
        
#     return Response(serializer.data)


# @api_view(["GET"])
# def get_Genre(request,genre=genre):
#     objects = Anime.objects.filter(genre)
#     serializer = AnimeSerializer(objects, many = True)
        
#     return Response(serializer.data)

def get_by_id( request,id):
    print(id)
    object = Anime.objects.get(id=id)
    serializer = AnimeSerializer(object, many = True)
    return Response(serializer.data)

def add_genre(request):
    li = [ 'Action', 'Adventure', 'Cars', 'Comedy', 'Dementia', 'Demons',
       'Drama', 'Ecchi', 'Fantasy', 'Game', 'Harem', 'Hentai',
       'Historical', 'Horror', 'Josei', 'Kids', 'Magic', 'Martial Arts',
       'Mecha', 'Military', 'Music', 'Mystery', 'Parody', 'Police',
       'Psychological', 'Romance', 'Samurai', 'School', 'Sci-Fi',
       'Seinen', 'Shoujo', 'Shoujo Ai', 'Shounen', 'Shounen Ai',
       'Slice of Life', 'Space', 'Sports', 'Super Power', 'Supernatural',
       'Thriller', 'Vampire', 'Yaoi', 'Yuri']
    for i in li:
         g = Genre(name = i)
         g.save()

    return HttpResponse("Done")


def add_animes(request):
    li = [ 'Action', 'Adventure', 'Cars', 'Comedy', 'Dementia', 'Demons',
        'Drama', 'Ecchi', 'Fantasy', 'Game', 'Harem', 'Hentai',
        'Historical', 'Horror', 'Josei', 'Kids', 'Magic', 'Martial Arts',
        'Mecha', 'Military', 'Music', 'Mystery', 'Parody', 'Police',
        'Psychological', 'Romance', 'Samurai', 'School', 'Sci-Fi',
        'Seinen', 'Shoujo', 'Shoujo Ai', 'Shounen', 'Shounen Ai',
        'Slice of Life', 'Space', 'Sports', 'Super Power', 'Supernatural',
        'Thriller', 'Vampire', 'Yaoi', 'Yuri']

        
        

    df = pd.read_csv(r"C:\Attiya\build\AnimeRecommenderApp\api\anime\anime.csv")
    for i in range(569,len(df)):
        try:
            df1 = dict(df.iloc[i,:])
            anime = Anime()
            anime.title = df1["title"]
            anime.synopsis = df1["synopsis"]
            # creating objs from genre
            objs = [Genre.objects.get(id=li.index(word.strip())+1)for word in df1["genre"].split(",")]
            
            anime.img_url = df1["img_url"]
            anime.aired = df1["aired"]
            anime.episodes = df1["episodes"]
            anime.ranked = df1["ranked"]
            anime.score = df1["score"]
           # anime.save()
            #you have to save before adding and use * instead of list
            anime.genre.add(*objs)
        except:
            pass
        
        
   




  

    return HttpResponse("Done")



from django.shortcuts import render, HttpResponse,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Genre,Anime
from .serializers import AnimeSerializer, GenreSerializer,UserSerialiser
from rest_framework.generics import CreateAPIView, ListAPIView , ListCreateAPIView, RetrieveDestroyAPIView
from .services import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication
class registerView(CreateAPIView):
    serializer_class = UserSerialiser
    




class SearchListApi(ListAPIView):
    queryset= Anime.objects.all()
    serializer_class = AnimeSerializer

    def get_queryset(self):
        qs  = self.queryset
        q = self.kwargs.get("q")
        print(q)
        q = q.replace("-"," ")
        if not q:
            return qs.none()
        return qs.search(q)


class RecommendApi(ListAPIView):
    serializer_class = AnimeSerializer
    lookup_field = "pk"
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs["pk"]
        recommended = most_similar(pk)
        anime_list = recommended.to_list()
        qs = Anime.objects.filter(title__in= anime_list).order_by("-score").distinct()

       #distinct(field) doesnt work for mysql 
        titles=[]
        qs_final = []
        for obj in qs:
            print(obj.title)
            if obj.title in titles:
                pass
            else:
                titles.append(obj.title)
                qs_final.append(obj)

                
       
        return qs_final


class AnimeCreateListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    queryset = Anime.objects.all().distinct()
    serializer_class = AnimeSerializer
    
class AnimeRUDApi(RetrieveDestroyAPIView):
    queryset = Anime.objects.all().distinct()
    serializer_class = AnimeSerializer
    lookup_field = "pk"
    

class GenreCreateListApi(ListCreateAPIView):
    queryset = Genre.objects.all().distinct()
    serializer_class = GenreSerializer


    

class GenreRUDApi(ListAPIView):
    serializer_class = AnimeSerializer
    lookup_field = "pk"
    queryset = Anime.objects.all().distinct()

    def get_queryset(self):
        pk = self.kwargs["pk"]  
        qs = Anime.objects.filter(genre__pk = pk) 
        return qs
        
    






# Create your views here.
# @api_view(["GET"])
# def recommend(request,pk):
#     recommended = most_similar(pk)
#     anime_list = recommended.to_list()
#     li = Anime.objects.filter(title__in= anime_list)
#     serializer = AnimeSerializer(li,many=True)

        
#     return Response(serializer.data) 






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



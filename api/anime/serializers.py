from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers, reverse
from .models import Anime,Genre
from django.contrib.auth.models import User


class UserSerialiser(ModelSerializer):
     password  = serializers.CharField(write_only=True)
     password1  = serializers.CharField(write_only=True)

     class Meta:
            model= User
            fields = ["username","email","password","password1"]

     def validate(self, attrs):
        if attrs["password1"] != attrs["password"]:
                 raise serializers.ValidationError({"password":"password fields dont match"})
                 
        return attrs
     def create(self, validated_data):
           user = User.objects.create(username = validated_data["username"],
           email = validated_data["email"]                      )
           user.set_password(validated_data["password"])
           user.save()
           return user

class AnimeSerializer(ModelSerializer):

   # recommend_url = serializers.HyperlinkedIdentityField(view_name="anime:recommend-view",
   #                                              lookup_field="pk" )
    recommend_url= serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Anime
        fields= ["id",'title', 'synopsis', 'genre', 'img_url', 'aired', 'episodes',
       'episodes', 'ranked', 'score',"recommend_url" ]
    def get_recommend_url(self,obj):
         request = self.context.get("request")
         if request is None:
               return None
         return reverse.reverse("anime:recommend-view",kwargs={"pk":obj.pk} ,request= request)

         
         
        
class AnimeInlineSerializer(serializers.Serializer):
      title = serializers.CharField(read_only =True)
      synopsis = serializers.CharField(read_only =True)
      img_url = serializers.CharField(read_only =True)
    
class GenreInlineSerializer(Serializer):
        animes = serializers.SerializerMethodField(read_only=True)
        def get_animes(self,obj):
            qs = obj.anime_set.all()
            return AnimeInlineSerializer(qs,many=True).data

    

class GenreSerializer(ModelSerializer):
   # animes = GenreInlineSerializer(read_only=True)
   # animes = serializers.SerializerMethodField(read_only=True)

   
    url = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Genre
        fields = ["name", "url"]

    # def get_animes(self,obj):
    #         qs = obj.anime_set.all()
    #         return AnimeSerializer(qs,many=True).data
    
    def get_url(self,obj):
        request = self.context.get("request")
        if request is None:
               return None

        return reverse.reverse("anime:detail-view",kwargs={"pk":obj.pk} ,request= request)
           

class GenreRetrieveSerializer(ModelSerializer):
    # animes = GenreInlineSerializer(read_only=True)
   # animes = serializers.SerializerMethodField(read_only=True)

   
    url = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Genre
        fields = ["animes"]

    # def get_animes(self,obj):
    #         qs = obj.anime_set.all()
    #         return AnimeSerializer(qs,many=True).data
    
    def get_url(self,obj):
        request = self.context.get("request")
        if request is None:
               return None

        return reverse.reverse("anime:detail-view",kwargs={"pk":obj.pk} ,request= request)
           
    
    
            
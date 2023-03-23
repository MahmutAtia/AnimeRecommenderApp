from django.db import models
from django.db.models import Q
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=128)

    @property
    def animes(self):
        return self.anime_set.all()

    def __str__(self):
        return self.name

class AnimeQuerySet(models.QuerySet):
    def search(self,query):
        lookup = Q(title__icontains=query)
        qs = self.filter(lookup)
        return qs

class AnimeManager(models.Manager):

    def get_queryset(self):
        return AnimeQuerySet(self.model,using=self.db)
    
    def search(self,query):
       return self.get_queryset().search(query)


class Anime(models.Model):
    title = models.CharField(max_length=128,default="",blank=True,null=True)
    synopsis = models.TextField(default="",null=True,blank=True)
    genre = models.ManyToManyField(Genre,null=True,blank=True)
    img_url = models.URLField(default="",null=True,blank=True)
    aired= models.CharField(max_length=128,default="",blank=True)
    episodes= models.FloatField(default="",null=True,blank=True)
    ranked=models.FloatField(default="",null=True,blank=True)
    score=models.FloatField(default="",null=True,blank=True)

    objects = AnimeManager()

    def __str__(self):
        return self.title
    
    

    class Meta:
        ordering = ["-score"]
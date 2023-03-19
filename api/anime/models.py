from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Anime(models.Model):
    title = models.CharField(max_length=128,default="",blank=True,null=True)
    synopsis = models.TextField(default="",null=True,blank=True)
    genre = models.ManyToManyField(Genre,null=True,blank=True)
    img_url = models.URLField(default="",null=True,blank=True)
    aired= models.CharField(max_length=128,default="",blank=True)
    episodes= models.FloatField(default="",null=True,blank=True)
    ranked=models.FloatField(default="",null=True,blank=True)
    score=models.FloatField(default="",null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-score"]
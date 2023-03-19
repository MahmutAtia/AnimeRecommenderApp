from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import AnimeApi

router = DefaultRouter()
router.register('',AnimeApi, basename="anime")


app_name = "anime"
urlpatterns = [
    path('', include(router.urls)),
    
]
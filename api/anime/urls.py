from django.urls import path,include
from .views import SearchListApi ,RecommendApi, AnimeCreateListApi,AnimeRUDApi,GenreCreateListApi,GenreRUDApi




app_name = "anime"
urlpatterns = [
    path('',AnimeCreateListApi.as_view() ),
    path('search/<slug:q>',SearchListApi.as_view()),
    path('<int:pk>/', AnimeRUDApi.as_view()),
    path('genre/',GenreCreateListApi.as_view()),
    path('genre/<int:pk>',GenreRUDApi.as_view(), name = "detail-view"),
    path('recommend/<int:pk>', RecommendApi.as_view(),name= "recommend-view")
    
]
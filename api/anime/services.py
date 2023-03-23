from .apps import  AnimeConfig
from .models import Anime
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

all_anime = AnimeConfig.all_anime
tf_idf = AnimeConfig.model
doc_dict = AnimeConfig.doc_dict
# anime = 'Fullmetal-Alchemist:-Brotherhood'

#doc = tf_idf.transform([])


def most_similar(pk): 
  print(pk)
  chosen_anime= Anime.objects.get(id = pk).title
  print(chosen_anime)
  anime_doc = doc_dict[chosen_anime]
  trans_doc = tf_idf.transform([anime_doc])
  simi_array = cosine_similarity(trans_doc, all_anime).flatten()
  simi_df = pd.DataFrame({
    "title":list(doc_dict.keys()) ,
    "similarity":simi_array 
                        })
  simi_df_sorted = simi_df.sort_values( by=["similarity"], ascending=False)
  
  return simi_df_sorted["title"][1:30]
from django.apps import AppConfig
import os
import pickle
from django.conf import settings


class AnimeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'anime'
    TRANSFORM_FILE = os.path.join(settings.MODELS, "all_animes_model.pkl")
    MODEL_FILE = os.path.join(settings.MODELS, "tf_idf.pkl")
    DICT_FILE = os.path.join(settings.MODELS, "doc_dict.pkl")

    with open(MODEL_FILE,'rb') as pkl:
        model = pickle.load(pkl)

    with open(TRANSFORM_FILE,'rb') as pkl:
        all_anime = pickle.load(pkl)

    with open(DICT_FILE,'rb') as pkl:
        doc_dict = pickle.load(pkl)

from sklearn.feature_extraction.text import TfidfVectorizer


from django.apps import AppConfig


from django.urls import path, include
from .views import *
urlpatterns = [

    path('get_habr', get_habr),
    path('check_link', check_link),
    path('set_article_on_db', set_article_on_db),
]
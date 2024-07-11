from django.urls import path
from ..views.api import (ArticleListCreateAPIView,
                         ArticleRetrieveUpdateDestroyAPIView,
                         GameListCreateAPIView,
                         GameRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('articles/', ArticleListCreateAPIView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', ArticleRetrieveUpdateDestroyAPIView.as_view(), name='article-detail'),
    path('games/', GameListCreateAPIView.as_view(), name='game-list-create'),
    path('games/<int:pk>/', GameRetrieveUpdateDestroyAPIView.as_view(), name='game-detail'),

]

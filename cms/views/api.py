from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import Article, Game
from ..serializers import ArticleSerializer, GameSerializer


class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ArticleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class GameListCreateAPIView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class GameRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
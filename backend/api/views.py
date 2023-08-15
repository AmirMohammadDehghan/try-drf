from rest_framework.generics import ListCreateAPIView
from .serializers import Article, ArticleSerialiser

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser
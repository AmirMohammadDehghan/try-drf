from rest_framework import serializers
from blog.models import Article

class ArticleSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ('title','slug','author','content','publish','status')
        # exclude =('created', 'updated')
        fields = "__all__"
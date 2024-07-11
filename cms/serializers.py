from rest_framework import serializers
from .models import Article, Game


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'genre', 'description', 'release_date', 'added_by']
        read_only_fields = ['added_by']

    def update(self, instance, validated_data):
        validated_data.pop('added_by', None)  # Remove added_by if present
        return super().update(instance, validated_data)


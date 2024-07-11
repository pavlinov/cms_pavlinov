from django import forms
from .models import Article, Game


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'genre', 'description', 'release_date']
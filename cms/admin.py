from django.contrib import admin

# Register your models here.

from .models import Article, Game

admin.site.register(Article)
admin.site.register(Game)
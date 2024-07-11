from django.urls import path

from .views.login_registration import (register_view, login_view, logout_view, index_view)
from .views.articles import (add_article_view, article_detail_view, article_list_view, remove_article_view, edit_article_view)
from .views.games import (game_list_view, add_game_view, edit_game_view, remove_game_view)

urlpatterns = [
    path('', index_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('article/add/', add_article_view, name='add_article'),
    path('article/<int:pk>/', article_detail_view, name='article_detail'),
    path('article/<int:pk>/edit/', edit_article_view, name='edit_article'),
    path('articles/', article_list_view, name='article_list'),
    path('article/<int:pk>/remove/', remove_article_view, name='remove_article'),

    path('games/', game_list_view, name='game_list'),
    path('game/add/', add_game_view, name='add_game'),
    path('game/<int:pk>/edit/', edit_game_view, name='edit_game'),
    path('game/<int:pk>/remove/', remove_game_view, name='remove_game'),

]

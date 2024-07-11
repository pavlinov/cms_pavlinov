from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import Client
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Game

class GameTests(TestCase):

    def setUp(self):
        #import ipdb; ipdb.set_trace()
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        #self.user = User.objects.create_user(username='testuser', password='testpassword')
        #self.client.force_authenticate(user=self.user)
        self.game_data = {
            'title': 'Test Game',
            'genre': 'Action',
            'description': 'Test Description',
            'release_date': '2023-01-01',
        }

    def test_create_game(self):
        game_data = dict(**self.game_data, added_by=self.user.id)
        response = self.client.post(reverse('game-list-create'), game_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 1)
        self.assertEqual(Game.objects.get().title, 'Test Game')

    def test_get_games(self):
        Game.objects.create(**self.game_data, added_by=self.user)
        response = self.client.get(reverse('game-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Game')

    def test_update_game(self):
        game = Game.objects.create(**self.game_data, added_by=self.user)
        updated_data = {
            'title': 'Updated Game',
            'genre': 'Adventure',
            'description': 'Updated Description',
            'release_date': '2023-02-01',
        }
        import ipdb; ipdb.set_trace()
        response = self.client.put(reverse('game-detail', kwargs={'pk': game.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        game.refresh_from_db()
        self.assertEqual(game.title, 'Updated Game')
        self.assertEqual(game.genre, 'Adventure')

    def test_delete_game(self):
        game = Game.objects.create(**self.game_data, added_by=self.user)
        response = self.client.delete(reverse('game-detail', kwargs={'pk': game.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Game.objects.count(), 0)


class GameViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.game_data = {
            'title': 'Test Game',
            'genre': 'Action',
            'description': 'Test Description',
            'release_date': '2023-01-01',
            'added_by': self.user
        }
        self.game = Game.objects.create(**self.game_data)

    def test_game_list_view(self):
        response = self.client.get(reverse('game_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Game')

    def test_add_game_view(self):
        response = self.client.get(reverse('add_game'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_game.html')

        response = self.client.post(reverse('add_game'), {
            'title': 'New Game',
            'genre': 'Puzzle',
            'description': 'New Description',
            'release_date': '2023-03-01'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Game.objects.count(), 2)
        self.assertEqual(Game.objects.last().title, 'New Game')

    def test_edit_game_view(self):
        response = self.client.get(reverse('edit_game', kwargs={'pk': self.game.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_game.html')

        response = self.client.post(reverse('edit_game', kwargs={'pk': self.game.pk}), {
            'title': 'Edited Game',
            'genre': 'RPG',
            'description': 'Edited Description',
            'release_date': '2023-04-01'
        })
        self.assertEqual(response.status_code, 302)
        self.game.refresh_from_db()
        self.assertEqual(self.game.title, 'Edited Game')

    def test_remove_game_view(self):
        response = self.client.get(reverse('remove_game', kwargs={'pk': self.game.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirm_delete.html')

        response = self.client.post(reverse('remove_game', kwargs={'pk': self.game.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Game.objects.count(), 0)

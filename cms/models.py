from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, {self.author}"


class Game(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
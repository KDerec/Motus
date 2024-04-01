from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class WordToGuess(models.Model):
    word_text = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.word_text}"

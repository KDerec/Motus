from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ranking = models.IntegerField(default=0)


class WordToGuess(models.Model):
    word_text = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.word_text}"


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    life_point = models.IntegerField(default=6)

    def __str__(self):
        return f"{self.user, self.life_point}"

    class Meta:
        constraints = [
            UniqueConstraint(fields=["user"], name="unique_game_per_user"),
        ]

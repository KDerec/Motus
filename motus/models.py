import requests

# from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class WordGenerator:
    def __init__(self):
        self.base_link = "https://random-word-api.herokuapp.com/word?lang=fr&&"

    def get_new_word(self, length):
        response = requests.get(self.base_link + f"length={length}")
        if response.status_code == 200:
            word = self.format_response(response.text)
            return word
        else:
            raise Exception(f"Erreur {response.status_code} : {response.text}")

    def format_response(self, response):
        return response.replace("[", "").replace("]", "").replace('"', "")

import random
import datetime as dt
from pathlib import Path
from django.db import models


class HeadsTails(models.Model):
    heads_tails = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Значение {self.heads_tails}, Дата создания: {self.time}"

    @staticmethod
    def counter(n: int):
        res = {"ОРЕЛ": 0,
               "РЕШКА": 0}
        heads = HeadsTails.objects.all()
        heads = heads[len(heads) - n:]
        for head in heads:
            if head.heads_tails == "ОРЕЛ":
                res["ОРЕЛ"] += 1
            elif head.heads_tails == "РЕШКА":
                res["РЕШКА"] += 1
        return res


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    autobiography = models.TextField()
    birthday = models.DateField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.birthday}"


class Article(models.Model):
    heading = models.CharField(max_length=200)
    content = models.TextField()
    date_publication = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    number_views = models.IntegerField(default=0)
    status_publication = models.BooleanField(default=False)

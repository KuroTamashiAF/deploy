from django.db import models


class HeadTails(models.Model):
    result = models.CharField(max_length=10)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Результат броска монеты: {self.result}"


class Cube(models.Model):
    result = models.IntegerField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Результат броска кубика: {self.result}"


class RandomNumber(models.Model):
    result = models.IntegerField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Результат рандома: {self.result}"

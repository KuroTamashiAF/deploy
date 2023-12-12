import random
from django.shortcuts import render
from django.http.response import HttpResponse
from heads_tails.models import HeadsTails


def heads_tails(request):
    game = ["ОРЕЛ", "РЕШКА"]
    responce = random.choice(game)
    obj = HeadsTails(heads_tails=responce)
    obj.save()
    return HttpResponse(obj)


def print_all_value(request, n: int):
    return HttpResponse(f'{HeadsTails.counter(n)}')

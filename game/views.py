from django.shortcuts import render, redirect
from .models import Cube, HeadTails, RandomNumber
from random import random, choice, randint
from .forms import ChoseGame
import logging

logger = logging.getLogger(__name__)


def heads_tails(request, count):
    game_lists = ["ОРЕЛ", "РЕШКА"]
    game_name = "Игра в монетку"
    for i in range(1, count):
        game_obj = HeadTails(result=choice(game_lists))
        game_obj.save()
    result = []
    game_obj_list = HeadTails.objects.all()
    for obj in game_obj_list[len(game_obj_list) - count:]:
        result.append(obj.result)
    return render(request, "game/universal.html", {"result_game": result,
                                                   "count": count,
                                                   "game_name": game_name})


def game_cube(request, count):
    game_name = "Игра в кубик"
    for numb in range(1, count):
        game_obj = Cube(result=randint(1, 6))
        game_obj.save()
    result = []
    game_obj_list = Cube.objects.all()
    for obj in game_obj_list[len(game_obj_list) - count:]:
        result.append(obj.result)
    return render(request, "game/universal.html", {"result_game": result,
                                                   "count": count,
                                                   "game_name": game_name})


def game_random_number(request, count):
    game_name = "Игра в угадай число"
    for numb in range(1, count):
        game_obj = RandomNumber(result=randint(1, 101))
        game_obj.save()
    result = []
    game_obj_list = RandomNumber.objects.all()
    for obj in game_obj_list[len(game_obj_list) - count:]:
        result.append(obj.result)
    return render(request, "game/universal.html", {"result_game": result,
                                                   "count": count,
                                                   "game_name": game_name})


def chose_game(request):
    if request.method == 'POST':
        form = ChoseGame(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            number_throws = form.cleaned_data['number_throws']
            logger.info(f"get {game}, {number_throws}")

            match game:
                case 'H':
                    return heads_tails(request, number_throws)
                case 'C':
                    return game_cube(request, number_throws)
                case 'R':
                    return game_random_number(request, number_throws)
    else:
        form = ChoseGame()
    return render(request, 'game/chose_game.html', {"form": form})

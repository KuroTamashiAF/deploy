from django.urls import path
from .views import heads_tails, game_cube, game_random_number, chose_game

urlpatterns = [
    path("heads/<int:count>/", heads_tails, name="heads_tails"),
    path("cube/<int:count>/", game_cube, name="cube"),
    path("randnumb/<int:count>/", game_random_number, name="random_number"),
    path('chose_game/', chose_game, name='chose_game'),

]

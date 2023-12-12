from django import forms


class ChoseGame(forms.Form):
    game = forms.ChoiceField(choices=[('H', 'Head Tails'), ('C', 'Cube'), ('R', 'Random_number')])
    number_throws = forms.IntegerField(min_value=1, max_value=64)

from models.player import *
from models.player_list import *


class Game:
    def __init__(self, player_list, player):

        if player_1.choice == player_2.choice:
            return None

        elif player_1.choice == "Rock":
            if player_2.choice == "Paper":
                return player_2
            if player_1.choice == "Scissors":
                return player_1

        elif player_1.choice == "Paper":
            if player_2.choice == "Rock":
                return player_1
            if player_1.choice == "Scissors":
                return player_2

        elif player_1.choice == "Scissors":
            if player_2.choice == "Rock":
                return player_2
            if player_1.choice == "Paper":
                return player_1

from flask import render_template, request
from app import app
from models.player import *
from models.player_list import players

@app.route("/")
def index():
    return render_template ("index.html", title="Home", players=players)

# @app.route('/rock/scissors')
# def game():
#     return "Player 1 wins by playing rock"

@app.route("/game")
def game(player_1, player_2):
    winner = f"The winner is {game(player_1, player_2)}"
    return render_template ("index.html", title="Game", players=players)
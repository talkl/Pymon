from bottle import (Bottle, request, jinja2_view, redirect)
from backend import utils
from backend import controller
from backend.db import getHighScores

pageHandler = Bottle()


@pageHandler.get('/start')
@jinja2_view('./backend/pages/start.html')
def start():
    currentPlayer = request.get_cookie("player")
    if currentPlayer:
        redirect("/games")
        return
    return {"version": utils.getVersion()}


@pageHandler.get('/games')
@jinja2_view('./backend/pages/games.html')
def games():
    currentPlayer = request.get_cookie("player")
    if not currentPlayer:
        redirect("/start")
        return
    return {"version": utils.getVersion(), "games": controller.listGames()}


@pageHandler.get('/games/<game_id>')
@jinja2_view('./backend/pages/game.html')
def play(game_id):
    currentPlayer = request.get_cookie("player")
    if not currentPlayer or not controller.gameExists(game_id):
        redirect("/start")
        return
    return {"version": utils.getVersion()}


@pageHandler.get('/')
@jinja2_view('./backend/pages/index.html')
def landing():
    return {"version": utils.getVersion()}


@pageHandler.get('/high-scores')
@jinja2_view('./backend/pages/high-scores.html')
def high_scores():
    top_10_high_scores = getHighScores()
    return {"highScores": top_10_high_scores, "version": utils.getVersion()}

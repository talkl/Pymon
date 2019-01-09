from bottle import (Bottle, static_file)
staticHandler = Bottle()

@staticHandler.get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./frontend/dist")

@staticHandler.get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./frontend/css")

@staticHandler.get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./frontend/images")

@staticHandler.get('/favicon.ico')
def get_favicon():
    return static_file('favicon.ico', root='./')

@staticHandler.get("/sounds/<filepath:re:.*\.mp3>")
def mp3(filepath):
    return static_file(filepath, root="./frontend/sounds")
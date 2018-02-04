from flask import Flask, request
from .route_handlers import test
import os

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY='development key'
    ))

@app.route('/')
def serve_spa():
    '''Serving the single page application to a client'''
    return app.send_static_file('index.html')

@app.route('/add')
def add_something():
    '''Test'''
    test.add_item()
    return os.getcwd()
    #return "Successfully added an item"

@app.route('/show')
def show():
    '''test'''
    return str(test.get_coll())

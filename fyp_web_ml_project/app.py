from flask import Flask, request
from .route_handlers import test

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY='development key'
))


@app.route('/')
def serve_spa():
    '''Serving the single page application to a client'''
    return app.send_static_file('index.html')


@app.route('/mlmodels/<ml_id>', methods=['PUT', 'POST'])
def train_model(ml_id):
    '''Machine learning model routes'''
    if request.method == 'POST':
        return "You just passed " + ml_id + " via POST"
    else:
        return "You just passed " + ml_id + " via PUT"


@app.route('/mlmodels/<ml_id>/predictions', methods=['GET', 'POST'])
def predict_model(ml_id):
    '''Machine learning model routes'''
    if request.method == 'POST':
        return "You just passed " + ml_id + " via POST"
    else:
        return "You just passed"


@app.route('/mlmodels/<ml_id>/created')
def is_model_create(ml_id):
    '''Machine learning model routes'''
    return "You just passed"


@app.route('/mlalgorithms')
def get_ml_algorithms():
    '''Return a list of available algorithms and their information'''
    return "Here's supposed to be some data"


@app.route('/dataset', methods=['POST'])
def query_data_set():
    '''Return result for a dataset query'''
    return "Here's supposed to be some data"


@app.route('/add')
def add_something():
    '''Test'''
    test.add_item()
    return 'Successfully added item'


@app.route('/show')
def show():
    '''test'''
    return str(test.get_coll())

from flask import Flask, request, jsonify
from .route_handlers import mlmodels, dataset, mlalgorithms
from .ml_ops import NotFoundMlClassError, NotFoundMlModelError,\
UntrainedMlModelError

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
    json_body = request.get_json(force=True)
    if request.method == 'POST':
        mlmodels.create_model(
            ml_id, json_body['ml_class_name'], json_body['settings_json'], json_body['dataset_query_json'])
        obj = {'ok': True, 'message': "{0} has been created".format(ml_id)}
        return jsonify(obj)
    elif request.method == 'PUT':
        mlmodels.reconfigure_model(
            ml_id, json_body['settings_json'], json_body['dataset_query_json'])
        obj = {'ok': True,
               'message': "{0} has been reconfigured".format(ml_id)}
        return jsonify(obj)
    else:
        raise Exception("The method you used is wrong")


@app.route('/mlmodels/<ml_id>/predictions', methods=['GET', 'POST'])
def predict_model(ml_id):
    '''Machine learning model routes'''
    # Get a prediction
    if request.method == 'POST':
        features_values_json = request.get_json(force=True)
        prediction = mlmodels.get_prediction_from_model(
            ml_id, features_values_json)
        return jsonify({'prediction': prediction})
    # Get a schema representing prediction features form
    else:
        features_form = mlmodels.get_prediction_factors_form_from_model(ml_id)
        return jsonify(features_form)


@app.route('/mlmodels/<ml_id>/created')
def is_model_create(ml_id):
    '''Machine learning model routes'''
    obj = {'created': mlmodels.is_model_created(ml_id)}
    return jsonify(obj)


@app.route('/mlalgorithms')
def get_ml_algorithms():
    '''Return a list of available algorithms and their information'''
    return jsonify(mlalgorithms.get_class_and_settings_dict())


@app.route('/dataset', methods=['POST'])
def query_data_set():
    '''Return result for a dataset query'''
    query_json = request.get_json(force=True)
    return jsonify(dataset.query_data_set(query_json))

# Error handlers for certain expressions
@app.errorhandler(NotFoundMlModelError)
def handle_not_found_model(exc):
    obj = {'message': str(exc)}
    return jsonify(obj), 404


@app.errorhandler(NotFoundMlClassError)
def handle_not_found_class(exc):
    obj = {'message': str(exc)}
    return jsonify(obj), 404

@app.errorhandler(UntrainedMlModelError)
def handle_untrained_ml_model(exc):
    obj = {'message': str(exc)}
    return jsonify(obj), 500

from flask import Flask, request, jsonify
from .route_handlers import mlmodels, dataset, mlalgorithms, mlclass
import fyp_web_ml_project.exceptions_collection as exc_coll

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


@app.route('/mlalgorithms/<ml_name>/score', methods=['POST'])
def get_score_from_ml_algorithm(ml_name):
    '''Return a score after running tests on the algorithm.'''
    json_obj = request.get_json(force=True)
    settings_json = json_obj['settings_json']
    dataset_query_json = json_obj['dataset_query_json']
    number_of_runs = json_obj['number_or_runs']
    perc_of_split = json_obj['perc_of_split']
    score = mlalgorithms.get_score_from_ml_algorithm(ml_name, settings_json,
                                                     dataset_query_json,
                                                     number_of_runs,
                                                     perc_of_split)
    return jsonify({'score': score})

@app.route('/mlalgorithms/<ml_name>/best-params', methods=['POST'])
def get_best_parameters_from_ml_algorithm(ml_name):
    json_obj = request.get_json(force=True)
    parameters_grid = json_obj['parameters_grid']
    dataset_query_json = json_obj['dataset_query_json']
    result_dict = mlalgorithms.get_best_parameters_from_ml_algorithm(ml_name,
                                                                     parameters_grid,
                                                                     dataset_query_json)
    return jsonify({'result': result_dict})


@app.route('/dataset', methods=['POST'])
def query_data_set():
    '''Return result for a dataset query'''
    query_json = request.get_json(force=True)
    return jsonify(dataset.query_data_set(query_json))


@app.route('/mlclass/<class_name>', methods=['POST'])
def add_new_ml_class(class_name):
    '''Create a new class'''
    json_obj = request.get_json(force=True)
    class_code = json_obj['code']
    mlclass.add_new_ml_class(class_name, class_code)
    successful_status = {
        'ok': True, 'msg': "{0} class is added successfully".format(class_name)}
    return jsonify(successful_status)

# Error handlers for exceptions


@app.errorhandler(exc_coll.NotFoundMlModelError)
def handle_not_found_model(exc):
    return _jsonify_error_json(exc), 404


@app.errorhandler(exc_coll.NotFoundMlClassError)
def handle_not_found_class(exc):
    return _jsonify_error_json(exc), 404


@app.errorhandler(exc_coll.UntrainedMlModelError)
def handle_untrained_ml_model(exc):
    return _jsonify_error_json(exc), 500


@app.errorhandler(exc_coll.UnrecognisedTypeError)
def handle_unrecognised_type(exc):
    return _jsonify_error_json(exc), 500


@app.errorhandler(exc_coll.NotFourKeysError)
def handle_not_four_keys_error(exc):
    return _jsonify_error_json(exc), 500


@app.errorhandler(exc_coll.MissingQueryKeyInJsonError)
def handle_missing_query_key_in_json_error(exc):
    return _jsonify_error_json(exc), 500


@app.errorhandler(exc_coll.MissingSettingParameterJsonError)
def handle_missing_setting_parameter_json_error(exc):
    return _jsonify_error_json(exc), 500


@app.errorhandler(exc_coll.DuplicateMlClassName)
def handle_duplicate_ml_class_name_error(exc):
    return _jsonify_error_json(exc), 500


@app.errorhandler(exc_coll.ClassSyntaxError)
def handle_class_syntax_error(exc):
    return _jsonify_error_json(exc), 500


# @app.errorhandler(Exception)
# def handle_any_exception(exc):
    # return _jsonify_error_json(exc), 500


def _jsonify_error_json(exc):
    '''Format the exception for JSON output'''
    return jsonify({'message': str(exc)})

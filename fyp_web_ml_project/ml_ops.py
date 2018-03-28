import fyp_web_ml_project.ml_classes_collection.ml_class_collector as ml_class_collector
import fyp_web_ml_project.validator_utils as validator_utils

ml_class_dict = ml_class_collector.ML_CLASSES_DICT
ml_models_dict = {}


def get_ml_class_and_settings_list():
    '''Return a list of strings representing ML class names and their settings'''
    return [[class_name, get_ml_class_settings(class_name)]
            for class_name in ml_class_dict]


def add_new_ml_class(new_class_name, class_instance):
    if new_class_name not in ml_class_dict:
        ml_class_dict[new_class_name] = class_instance
    else:
        raise DuplicateMlClassName(new_class_name)


def get_ml_class_settings(ml_class_name):
    '''Return a machine learning algorithm settings in JSON format'''
    try:
        return ml_class_dict[ml_class_name]("get settings object").get_current_settings_parameters()
    except KeyError as exc:
        raise NotFoundMlClassError(ml_class_name) from exc


def is_model_created(ml_model_name):
    return ml_model_name in ml_models_dict


def get_model_parameters_dict(ml_model_name):
    '''Return a model's current parameter list'''
    try:
        return ml_models_dict[ml_model_name].get_settings_parameter_list()
    except KeyError as exc:
        raise NotFoundMlModelError(ml_model_name) from exc


def get_model_training_feature_list(ml_model_name):
    '''Return a list of features names and corresponding values that were used in training'''
    try:
        return ml_models_dict[ml_model_name].get_feature_names_and_values_list()
    except KeyError as exc:
        raise NotFoundMlModelError(ml_model_name) from exc


def train_ml_model(ml_model_name, features_list, training_set, target_set):
    '''Traing a model'''
    try:
        ml_models_dict[ml_model_name].train_model(
            features_list, training_set, target_set)
    except KeyError as exc:
        raise NotFoundMlModelError(ml_model_name) from exc


def get_prediction_from_model(ml_model_name, features_values_json):
    '''Get a prediction from a trained model'''
    try:
        model = ml_models_dict[ml_model_name]
        if not model.is_trained():
            raise UntrainedMlModelError(ml_model_name)
        return model.get_prediction_from_model(features_values_json)
    except KeyError as exc:
        raise NotFoundMlModelError(ml_model_name) from exc


def create_model(ml_model_name, ml_class_name, settings_json):
    '''Create a new model'''
    try:
        ml_class = ml_class_dict[ml_class_name]
        validator_utils.check_ml_settings_json(
            ml_class(ml_model_name).get_settings_parameter_list(), settings_json)
        ml_models_dict[ml_model_name] = ml_class(settings_json)
    except KeyError as exc:
        raise NotFoundMlClassError(ml_class_name) from exc


def reconfigure_model(ml_model_name, settings_json):
    '''Reconfigure existing model's algorithm settings'''
    try:
        model = ml_models_dict[ml_model_name]
        validator_utils.check_ml_settings_json(
            model.get_settings_parameter_list(), settings_json)
        model.reconfigure_class(settings_json)
    except KeyError as exc:
        raise NotFoundMlModelError(ml_model_name) from exc


def get_score_from_ml_algorithm(ml_class_name, settings_json, features_set, training_features_set, training_class_set, test_features_set, test_class_set):
    if ml_class_name not in ml_class_dict:
        raise NotFoundMlClassError(ml_class_name)

    ml_model_instance = ml_class_dict[ml_class_name](
        "for scoring", settings_json)
    ml_model_instance.train_model(
        features_set, training_features_set, training_class_set)
    return ml_model_instance.get_score_from_trained_model(test_features_set, test_class_set)


def get_best_parameters_from_algorithm(ml_class_name, parameters_dict, dataset_dict):
    if ml_class_name not in ml_class_dict:
        raise NotFoundMlClassError(ml_class_name)
    return ml_class_dict[ml_class_name]('getting best params').get_best_parameters_from_algorithm(parameters_dict, dataset_dict)

# List of exceptions


class Error(Exception):
    def __str__(self):
        return self.message


class NotFoundMlClassError(Error):
    def __init__(self, class_name):
        self.message = "{0} is not in the ML class list".format(class_name)


class NotFoundMlModelError(Error):
    def __init__(self, model_name):
        self.message = "{0} is not in the ML created models list".format(
            model_name)


class UntrainedMlModelError(Error):
    def __init__(self, model_name):
        self.message = "{0} is not trained with data".format(model_name)


class DuplicateMlClassName(Error):
    def __init__(self, class_name):
        self.message = "{0} already exists within the ml classes.".format(
            class_name)

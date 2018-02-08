import fyp_web_ml_project.ml_classes_collection.ml_class_collector as ml_class_collector
import fyp_web_ml_project.validator_utils as validator_utils

ml_class_dict = ml_class_collector.ML_CLASSES_DICT
ml_models_dict = {}


def get_ml_class_and_settings_list():
    '''Return a list of strings representing ML class names and their settings'''
    return [[class_name, get_ml_class_settings(class_name)]
            for class_name in ml_class_dict]


def get_ml_class_settings(ml_class_name):
    '''Return a machine learning algorithm settings in JSON format'''
    try:
        return ml_class_dict[ml_class_name]("get settings object").get_current_settings_parameters()
    except KeyError:
        raise NotFoundMlClassError(ml_class_name)


def is_model_created(ml_model_name):
    return ml_model_name in ml_models_dict


def get_model_parameters_dict(ml_model_name):
    '''Return a model's current parameter list'''
    return ml_models_dict[ml_model_name].get_settings_parameter_list()


def get_model_training_feature_list(ml_model_name):
    '''Return a list of features lists that were used in training'''
    return ml_models_dict[ml_model_name].get_feature_names_list()


def train_ml_model(ml_model_name, features_list, training_set, target_set):
    '''Traing a model'''
    try:
        ml_models_dict[ml_model_name].train_model(
            features_list, training_set, target_set)
    except KeyError:
        raise NotFoundMlModelError(ml_model_name)


def get_prediction_from_model(ml_model_name, features_values_json):
    '''Get a prediction from a trained model'''
    try:
        model = ml_models_dict[ml_model_name]
        if not model.is_trained():
            raise UntrainedMlModelError(ml_model_name)
        return model.get_prediction_from_model(features_values_json)
    except KeyError:
        raise NotFoundMlModelError(ml_model_name)


def create_model(ml_model_name, ml_class_name, settings_json):
    '''Create a new model'''
    try:
        ml_class = ml_class_dict[ml_class_name]
        validator_utils.check_ml_settings_json(
            ml_class().get_settings_parameter_list(), settings_json)
        ml_models_dict[ml_model_name] = ml_class(settings_json)
    except KeyError:
        raise NotFoundMlClassError(ml_class_name)


def reconfigure_model(ml_model_name, settings_json):
    '''Reconfigure existing model's algorithm settings'''
    try:
        model = ml_models_dict[ml_model_name]
        validator_utils.check_ml_settings_json(
            model.get_settings_parameter_list(), settings_json)
        model.reconfigure_class(settings_json)
    except KeyError:
        raise NotFoundMlModelError(ml_model_name)

# List of exceptions


class Error(Exception):
    pass


class NotFoundMlClassError(Error):
    def __init__(class_name):
        self.message = "{0} is not in the ML class list".format(class_name)


class NotFoundMlModelError(Error):
    def __init__(model_name):
        self.message = "{0} is not in the ML created models list".format(
            model_name)


class UntrainedMlModelError(Error):
    def __init__(model_name):
        self.message = "{0} is not trained with data".format(model_name)

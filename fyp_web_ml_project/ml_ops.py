import fyp_web_ml_project.ml_classes_collection.ml_class_collector as ml_class_collector

ml_class_dict = ml_class_collector.ML_CLASSES_DICT
ml_trained_models_dict = {}


def show_class_dict():
    print(ml_class_dict)


def get_ml_class_list():
    '''Return a list of strings representing ML class names'''
    return list(ml_class_dict.keys())


def get_ml_class_settings(ml_class_name):
    '''Return a machine learning algorithm settings in JSON format'''
    try:
        return ml_class_dict[ml_class_name]("get settings object").get_current_settings_parameters()
    except KeyError:
        raise Exception("{0} is not in the ML class list".format(ml_class_name))
#def get_prediction_from_model(ml_model_id, features_values_json)

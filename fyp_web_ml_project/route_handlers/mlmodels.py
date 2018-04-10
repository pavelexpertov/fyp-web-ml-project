import fyp_web_ml_project.ml_ops as ml_ops
import fyp_web_ml_project.db as db
import fyp_web_ml_project.validator_utils as validator_utils
from fyp_web_ml_project.json_form_utils import create_json_schema_field


def create_model(model_name, ml_class_name, settings_json, dataset_query_json):
    # Create a simple model with custom settings
    ml_ops.create_model(model_name, ml_class_name, settings_json)
    # Train the model with training and target sets
    validator_utils.check_query_json(dataset_query_json)
    store_number = dataset_query_json['store_number']
    features_list = dataset_query_json['features_list']
    end_date = dataset_query_json['end_date']
    start_date = dataset_query_json['start_date']
    set_dict = db.get_training_and_target_set(
        store_number, features_list, start_date, end_date)
    ml_ops.train_ml_model(model_name, features_list,
                          set_dict['training_set'], set_dict['target_set'])


def reconfigure_model(model_name, settings_json, dataset_query_json):
    ml_ops.reconfigure_model(model_name, settings_json)
    # Train the model with training and target sets
    validator_utils.check_query_json(dataset_query_json)
    store_number = dataset_query_json['store_number']
    features_list = dataset_query_json['features_list']
    end_date = dataset_query_json['end_date']
    start_date = dataset_query_json['start_date']
    set_dict = db.get_training_and_target_set(
        store_number, features_list, start_date, end_date)
    ml_ops.train_ml_model(model_name, features_list,
                          set_dict['training_set'], set_dict['target_set'])


def is_model_created(model_name):
    return ml_ops.is_model_created(model_name)


def get_built_model_params(model_name):
    return ml_ops.get_model_parameters_dict(model_name)


def get_prediction_from_model(model_name, features_values_json):
    return ml_ops.get_prediction_from_model(model_name, features_values_json)


def get_prediction_factors_form_from_model(model_name):
    feature_dict_list = ml_ops.get_model_training_feature_list(model_name)
    feature_dict = {}
    for iter_feature_dict in feature_dict_list:
        feature_dict = {**feature_dict, **iter_feature_dict}

    feature_values_schema_list = []
    for key, value in feature_dict.items():
        schema_field = create_json_schema_field(key, value)
        feature_values_schema_list.append(schema_field)

    feature_values_schema_dict = {'fields': feature_values_schema_list}
    form_dict = {
        'features_values': feature_dict,
        'features_values_schema': feature_values_schema_dict
    }
    return form_dict

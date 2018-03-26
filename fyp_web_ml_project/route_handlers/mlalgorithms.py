from sklearn.model_selection import train_test_split

import fyp_web_ml_project.ml_ops as ml_ops
from fyp_web_ml_project.json_form_utils import create_json_schema_field
from fyp_web_ml_project.db import get_training_and_target_set


def get_class_and_settings_dict():
    ml_list = ml_ops.get_ml_class_and_settings_list()
    new_list = []
    for cls_name, property_dict in ml_list:
        fields_list = [create_json_schema_field(name, value) for name, value in
                       property_dict.items()]
        json_form_fields_dict = {'fields': fields_list}
        obj = {
            'name': cls_name,
            'settings_values': property_dict,
            'settings_form_schema': json_form_fields_dict
        }
        new_list.append(obj)
    return new_list


def get_score_from_ml_algorithm(ml_name, settings_json, dataset_query_json, number_of_runs, perc_of_split):
    dataset = get_training_and_target_set(dataset_query_json['store_number'],
                                          dataset_query_json['features_list'],
                                          dataset_query_json['start_date'],
                                          dataset_query_json['end_date'])
    counters = {}
    features_list = dataset_query_json['features_list']
    for num in range(number_of_runs):
        (training_features_list, test_features_list, training_classes_list,
         test_classes_list) = train_test_split(dataset['training_set'],
                                               dataset['target_set'],
                                               train_size=perc_of_split)
        score = ml_ops.get_score_from_ml_algorithm(ml_name, settings_json,
                                                   dataset_query_json['features_list'],
                                                   training_features_list,
                                                   training_classes_list,
                                                   test_features_list,
                                                   test_classes_list)
        score = round(score, 2)
        if score not in counters:
            counters[score] = 1
        else:
            counters[score] = counters[score] + 1

    return counters

import fyp_web_ml_project.db as db
import fyp_web_ml_project.validator_utils as validator_utils

def query_data_set(query_json):
    '''Query database and returns a list of datasets'''
    validator_utils.check_query_json(query_json)
    features_list = query_json['features_list']
    start_date = query_json['start_date']
    end_date = query_json['end_date']
    store_number = query_json['store_number']
    return db.get_store_dataset_json_list(store_number, features_list, start_date, end_date)

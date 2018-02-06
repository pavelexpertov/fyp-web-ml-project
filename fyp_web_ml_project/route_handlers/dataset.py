import fyp_web_ml_project.db as db

def query_data_set(query_json):
    '''Query database and returns a list of datasets'''
    key_list = ['features_list', 'start_date', 'end_date', 'store_number']
    if len(query_json.keys()) != len(key_list):
        raise Exception("There's supposed to be 4 keys rather than {0}".format(len(query_json.keys())))
    query_key_list = query_json.keys()
    for key in key_list:
        if key not in query_key_list:
            raise Exception("A query key doesn't exist in the json: " + key)

    features_list = query_json['features_list']
    start_date = query_json['start_date']
    end_date = query_json['end_date']
    store_number = query_json['store_number']
    return db.get_store_dataset_json_list(store_number, features_list, start_date, end_date)

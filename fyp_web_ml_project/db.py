import pandas as pd
import pymongo

CLIENT = pymongo.MongoClient()
START_DATE = '2010-02-05'
END_DATE = '2012-11-01'


def get_training_and_target_set(store_number, features_list, start_date=START_DATE, end_date=END_DATE):
    '''Return training and targets datasets based on search query

    It includes WeeklySales by default in order to separate a target set from training set.
    '''
    if len(features_list) == 0:
        raise Exception("features_list needs to have more than 0 items.")
    features_list = features_list.copy()
    SALES_KEY = 'WeeklySales'
    if SALES_KEY not in features_list:
        features_list.append(SALES_KEY)
    data_set_list = get_store_dataset_json_list(
        store_number, features_list, start_date, end_date)
    data_frame = pd.io.json.json_normalize(
        data_set_list, meta_prefix=features_list)
    # Extracting target set
    target_array = data_frame[SALES_KEY].values
    features_list.remove(SALES_KEY)
    # Extracting training set
    data_frame = data_frame[features_list]
    training_array = data_frame.values
    return {'target_set': target_array, 'training_set': training_array}


def get_store_dataset_json_list(store_number, features_list, start_date=START_DATE, end_date=END_DATE):
    '''Return a list of dataset for a store in a json format'''
    if len(features_list) == 0:
        raise Exception("features_list needs to have more than 0 items.")
    db = CLIENT.data_set
    collection = db.sales
    search_query = {'Date': {'$gte': start_date,
                             '$lte': end_date}, 'Store': store_number}
    key_selection_dict = {'_id': 0}
    for key in features_list:
        key_selection_dict[key] = 1
    cursor = collection.find(search_query, key_selection_dict)
    data_set_list = list(cursor)
    return data_set_list

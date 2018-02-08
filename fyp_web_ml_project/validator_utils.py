
def check_query_json(query_json):
    '''Check query keys for when performing a query against a database'''
    key_list = ['features_list', 'start_date', 'end_date', 'store_number']
    if len(query_json.keys()) != len(key_list):
        raise Exception("There's supposed to be 4 keys rather than {0}".format(
            len(query_json.keys())))
    query_key_list = query_json.keys()
    for key in key_list:
        if key not in query_key_list:
            raise Exception("A query key doesn't exist in the json: " + key)


def check_ml_settings_json(ml_parameters_list, passed_parameters_dict):
    '''Check passed parameters list against the actual parameters'''
    for parameter in passed_parameters_dict:
        if parameter not in ml_parameters_list:
            raise Exception(
                '{0} is not in passed settings parameters'.format(parameter))

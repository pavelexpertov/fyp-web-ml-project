
def check_query_json(query_json):
    '''Check query keys for when performing a query against a database'''
    key_list = ['features_list', 'start_date', 'end_date', 'store_number']
    if len(query_json.keys()) != len(key_list):
        raise NotFourKeysError(len(query_json.keys()))
    query_key_list = query_json.keys()
    for key in key_list:
        if key not in query_key_list:
            raise MissingQueryKeyInJsonError(key)


def check_ml_settings_json(ml_parameters_list, passed_parameters_dict):
    '''Check passed parameters list against the actual parameters'''
    for parameter in passed_parameters_dict:
        if parameter not in ml_parameters_list:
            raise MissingSettingParameterJsonError(parameter)


class Error(Exception):
    def __str__(self):
        return self.message


class NotFourKeysError(Error):
    def __init__(self, number_of_keys):
        self.message = "There's supposed to be 4 keys rather than {0} in query json".format(
            number_of_keys)


class MissingQueryKeyInJsonError(Error):
    def __init__(self, missing_key):
        self.message = "A query key doesn't exist in the json: " + missing_key


class MissingSettingParameterJsonError(Error):
    def __init__(self, missing_parameter):
        self.message = '{0} from passed settings parameters list is not in the actual list of parameters'.format(
            missing_parameter)

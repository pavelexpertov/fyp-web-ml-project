
def create_json_schema_field(field_name, actual_value, required=True):
    schema_field_dict = {
        'required': required,
        'type': "input",
        'label': field_name,
        'model': field_name
    }
    if type(actual_value) is str:
        schema_field_dict['inputType'] = 'text'
    elif type(actual_value) is int or type(actual_value) is float:
        schema_field_dict['inputType'] = 'number'
    else:
        raise UnrecognisedTypeError(actual_value, field_name)
    return schema_field_dict


# Exceptions
class Error(Exception):
    def __str__(self):
        return self.message


class UnrecognisedTypeError(Error):
    def __init__(self, value, field_name):
        value_type = type(value)
        self.message = "Unrecognised Type -- FieldName: {2}, Value: {0}, Its Type: {1}".format(
            value, value_type, field_name)

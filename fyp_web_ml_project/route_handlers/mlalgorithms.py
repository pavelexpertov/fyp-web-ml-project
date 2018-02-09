import fyp_web_ml_project.ml_ops as ml_ops
from fyp_web_ml_project.json_form_utils import create_json_schema_field


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

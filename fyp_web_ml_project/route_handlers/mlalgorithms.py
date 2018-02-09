import fyp_web_ml_project.ml_ops as ml_ops

def get_class_and_settings_dict():
    return [{'name': cls_name, 'propert_dict': property_dict}
            for cls_name, property_dict in ml_ops.get_ml_class_and_settings_list()]

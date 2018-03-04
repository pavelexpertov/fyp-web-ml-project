"""The purpose of the module is to formalise entered code and add it to ml_ops's module"""

import sklearn
import fyp_web_ml_project.ml_ops as ml_ops
from fyp_web_ml_project.ml_classes_collection.ml_classes.abstract_ml_class import AbstractMlClass


def add_new_ml_class(new_class_name, class_code):
    try:
        exec(class_code)
        created_class_instance = locals()[new_class_name]
        test_instance = created_class_instance('just a test')
    except Exception as exc:
        raise ClassSyntaxError(str(exc)) from exc
    else:
        created_class_instance = locals()[new_class_name]
        ml_ops.add_new_ml_class(new_class_name, created_class_instance)


class Error(Exception):
    def __str__(self):
        return self.message


class ClassSyntaxError(Error):
    def __init__(self, message):
        self.message = message

"""The purpose of the module is to formalise entered code and add it to ml_ops's module"""

import fyp_web_ml_project.ml_ops as ml_ops
from fyp_web_ml_project.ml_classes_collection.ml_classes.abstract_ml_class import AbstractMlClass


def add_new_ml_class(new_class_name, class_code):
    try:
        exec(class_code)
    except (NameError, TypeError, IndentationError) as exc:
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

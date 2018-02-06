'''Generates a dictionary containing user defined machine learning
classes'''
from fyp_web_ml_project.ml_classes_collection.ml_classes import *

ml_class_list = [local_key for local_key in locals()
                 if local_key.endswith('ML')]
local_dict = locals()
ML_CLASSES_DICT = {}
for ml_class_name in ml_class_list:
    ML_CLASSES_DICT[ml_class_name] = local_dict[ml_class_name]

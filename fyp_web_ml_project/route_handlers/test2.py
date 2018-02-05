import fyp_web_ml_project.ml_ops as ml_ops
import random


def add_item():
    ml_ops.add_item(random.random(), random.random())

def get_coll():
    return len(ml_ops.get_coll().keys())

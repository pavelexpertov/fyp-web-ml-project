from sklearn.tree import DecisionTreeRegressor

from fyp_web_ml_project.ml_classes_collection.ml_classes.abstract_ml_class import AbstractMlClass

class DecisionTreesML(AbstractMlClass):

    def __init__(self, name, settings_json=''):
        if settings_json:
            super().__init__(name, DecisionTreeRegressor(**settings_json))
        else:
            super().__init__(name, DecisionTreeRegressor())

    def printOut(self):
        print(self.name)

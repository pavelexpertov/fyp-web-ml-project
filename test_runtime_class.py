from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV

from fyp_web_ml_project.ml_classes_collection.ml_classes.abstract_ml_class import AbstractMlClass


class LassoML(AbstractMlClass):

    def __init__(self, name, settings_json=''):
        if settings_json:
            super().__init__(name, Lasso(**settings_json))
        else:
            super().__init__(name, Lasso())

    def reconfigure_class(self, settings_json):
        self.remove_features_names_list()
        self.estimator = DecisionTreeRegressor(**settings_json)

    def get_best_parameters_from_algorithm(self, parameter_grid, dataset_dict):
        '''Return a dict with best parameters'''
        training_feature_set = dataset_dict['training_feature_set']
        training_class_set = dataset_dict['training_class_set']
        estimator = Lasso()
        grid_search = GridSearchCV(estimator, param_grid=parameter_grid)
        grid_search.fit(training_feature_set, training_class_set)
        return {
            'best_params': grid_search.best_params_,
            'best_score': grid_search.best_score_
        }

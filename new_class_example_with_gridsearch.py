# Pretend that the imoprt statement is already executed: import sklearn

class ElasticNetML(AbstractMlClass):
    def __init__(self, name, settings_json=''):
        '''Default constructor: the conditions must be the same to accomodate for default and
        optional settings of the algorithm'''
        if settings_json:
            super().__init__(name, sklearn.linear_model.ElasticNet(**settings_json))
        else:
            super().__init__(name, sklearn.linear_model.ElasticNet())

    def get_best_parameters_from_algorithm(self, parameter_grid, dataset_dict):
        '''Return a dict with best parameters'''
        training_feature_set = dataset_dict['training_feature_set']
        training_class_set = dataset_dict['training_class_set']
        estimator = sklearn.linear_model.ElasticNet()
        grid_search = sklearn.model_selection.GridSearchCV(estimator, param_grid=parameter_grid)
        grid_search.fit(training_feature_set, training_class_set)
        return {
            'best_params': grid_search.best_params_,
            'best_score': grid_search.best_score_
        }

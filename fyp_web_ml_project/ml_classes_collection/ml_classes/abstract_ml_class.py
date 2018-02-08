class AbstractMlClass:

    def __init__(self, name, estimator):
        self.name = name
        self.estimator = estimator

    def get_name(self):
        return self.name

    def get_estimator(self):
        return self.estimator

    def get_feature_names_list(self):
        return self.feature_names_list

    def get_current_settings_parameters(self):
        return self.estimator.get_params()

    def get_settings_parameter_list(self):
        return list(self.get_current_settings_parameters().keys())

    def train_model(self, feature_names_list, features_training_list, target_list):
        '''Train a model and remember the order of the list of feature names'''
        self.feature_names_list = feature_names_list
        self.estimator.fit(features_training_list, target_list)

    def get_prediction_from_model(self, features_prediction_values_json):
        '''Return a predicted value based on provided prediction values'''
        fd = features_prediction_values_json
        features_list = [fd[feature_name] for feature_name in self.get_feature_names_list()]
        return self.estimator.predict(features_prediction_values_list)

    def reconfigure_class(self, settings_json):
        raise Exception('Implement reconfigure_class method')

    def remove_features_names_list(self):
        '''Remove a feature_names_list property from an instance'''
        if hasattr(self, 'feature_names_list'):
            del self.feature_names_list

    def is_trained(self):
        '''Return boolean whether a model is trained or not'''
        return hasattr(self, 'feature_names_list')

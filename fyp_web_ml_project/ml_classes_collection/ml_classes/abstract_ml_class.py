class AbstractMlClass:

    def __init__(self, name, estimator):
        self.name = name
        self.estimator = estimator

    def get_name(self):
        return self.name

    def get_estimator(self):
        return self.estimator

    def get_current_settings_parameters(self):
        raise Exception('Implement get_current_settings_parameters method')

    def train_model(self):
        raise Exception('Implement train_model method')

    def get_prediction_from_model(self):
        raise Exception('Implement get_prediction_from_model method')

    def reconfigure_class(self):
        raise Exception('Implement reconfigure_class method')

    def get_vue_form_schema(self):
        raise Exception('Implement get_vue_form_schema method')

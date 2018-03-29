# Pretend that the imoprt statement is already executed: import sklearn

class ElasticNetML(AbstractMlClass):
    def __init__(self, name, settings_json=''):
        '''Default constructor: the conditions must be the same to accomodate for default and
        optional settings of the algorithm'''
        if settings_json:
            super().__init__(name, sklearn.linear_model.ElasticNet(**settings_json))
        else:
            super().__init__(name, sklearn.linear_model.ElasticNet())

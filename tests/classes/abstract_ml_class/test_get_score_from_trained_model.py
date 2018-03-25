import unittest
from unittest.mock import Mock

import fyp_web_ml_project.ml_classes_collection.ml_classes.abstract_ml_class\
    as abstract_ml_class


class MockClass(abstract_ml_class.AbstractMlClass):
    '''Used to inherit methods and properties from the abstract class in order to inherit methods from it
    and test in actual used conditions'''

    def __init__(self, name):
        self.mock_obj = Mock()
        super().__init__(name, self.mock_obj)


class TestAbstractClassGetScoreFromTrainedModel(unittest.TestCase):
    def setUp(self):
        # Setting up an instance of the MockClass
        self.instance_name = "test class"
        self.test_mock_instance = MockClass(self.instance_name)
        self.training_features_name_list = ['blah', '2']
        self.training_feature_set = [[23, 23], [23, 43]]
        self.training_class_set = [1, 2]
        self.test_feature_set = [[12, 54], [52, 98]]
        self.test_class_set = [2, 1]

    def test_raising_untrained_model_exception(self):
        '''Test when the function is called and an exception is raised'''
        with self.assertRaises(abstract_ml_class.UntrainedModelError) as cm:
            self.test_mock_instance.get_score_from_trained_model(self.test_feature_set, self.test_class_set)

    def test_passing_values_to_score_function_correctly(self):
        '''Test passing the values to the score function correctly'''
        self.test_mock_instance.train_model(
            self.training_features_name_list, self.training_feature_set, self.training_class_set)
        self.test_mock_instance.get_score_from_trained_model(
            self.test_feature_set, self.test_class_set)
        self.test_mock_instance.estimator.score.assert_called_once_with(self.test_feature_set, self.test_class_set)

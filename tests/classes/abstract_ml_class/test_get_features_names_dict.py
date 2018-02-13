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


class TestAbstractClassGetFeatureNamesDictFunction(unittest.TestCase):
    def setUp(self):
        # Setting up an instance of the MockClass
        self.test_mock_instance = MockClass("test class")

    def test_correct_returned_dict(self):
        '''Test returned dict with correct values'''

        # Need to call train_model in order to set up certain properties
        test_feature_names_list = ['test_name1', 'test_name2']
        test_features_training_list = [[23, 45], [234, 9834]]
        test_target_list = [8934, 9000]
        self.test_mock_instance.train_model(
            test_feature_names_list, test_features_training_list, test_target_list)
        # Getting the result
        test_list = [{'test_name1': 23}, {'test_name2': 45}]
        returned_list = self.test_mock_instance.get_feature_names_and_values_list()
        self.assertEqual(returned_list, test_list, "Returned dict and a value test dict do not match")

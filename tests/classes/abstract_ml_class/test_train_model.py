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


class TestAbstractClassTrainModelFunction(unittest.TestCase):
    def setUp(self):
        # Setting up an instance of the MockClass
        self.test_mock_instance = MockClass("test class")

    def test_correctly_passed_values(self):
        '''Test that the values have been assigned correctly to estimator's methods'''

        test_feature_names_list = ['test_name1', 'test_name2']
        test_features_training_list = [[23, 45], [234, 9834]]
        test_target_list = [8934, 9000]
        test_feature_list_example = test_features_training_list[0]
        self.test_mock_instance.train_model(
            test_feature_names_list, test_features_training_list, test_target_list)
        # Testing certain class properties
        instance = self.test_mock_instance
        self.assertEqual(instance.feature_list_example, test_feature_list_example, 'feature_list_example and test value don\'t match')
        self.assertEqual(instance.feature_names_list, test_feature_names_list, 'feature_names_list and test value don\'t match')
        # Testing a class call
        mock_obj = self.test_mock_instance.mock_obj
        mock_obj.fit.assert_called_once_with(test_features_training_list, test_target_list)

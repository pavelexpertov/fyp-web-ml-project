import unittest
from unittest.mock import patch, Mock

import fyp_web_ml_project.ml_ops as ml_ops


class TestGetModelTrainingFeatureList(unittest.TestCase):

    def test_getting_feature_list_successfully(self):
        '''Test to make sure that the feature list is returned in a correct format'''
        test_dict_list = [{'test_key': 23}, {'test2': 45}]
        mock_instance = Mock()
        mock_instance.get_feature_names_and_values_list = Mock(
            return_value=test_dict_list)
        fake_ml_dict = {'test_name': mock_instance}
        with patch.dict('fyp_web_ml_project.ml_ops.ml_models_dict', values=fake_ml_dict):
            returned_list = ml_ops.get_model_training_feature_list('test_name')
        self.assertEqual(returned_list, test_dict_list,
                         "Returned list doesn't match")
        mock_instance.get_feature_names_and_values_list.assert_called_once()

    def test_raising_not_found_model_error(self):
        '''Test to make sure an exception is risen from not found model name'''
        test_dict_list = [{'test_key': 23}, {'test2': 45}]
        mock_instance = Mock()
        mock_instance.get_feature_names_and_values_list = Mock(
            return_value=test_dict_list)
        fake_ml_dict = {'test_name': mock_instance}
        with patch.dict('fyp_web_ml_project.ml_ops.ml_models_dict', values=fake_ml_dict):
            with self.assertRaises(ml_ops.NotFoundMlModelError) as cm:
                returned_list = ml_ops.get_model_training_feature_list(
                    'wrong_name')

        exc = cm.exception
        self.assertEqual("wrong_name is not in the ML created models list", str(
            exc), "The error message doesn't match")

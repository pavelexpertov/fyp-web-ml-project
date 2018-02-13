import unittest
from unittest.mock import Mock, patch

import fyp_web_ml_project.route_handlers.mlmodels as mlmodels


class TestMlmodelsRouterGetPredictionFActorsFormFromModel(unittest.TestCase):

    def test_correctly_formatted_dict(self):
        '''Test that the function returns correctly formatted dict from the model'''
        test_feature_values = [
            {
                'feature_name1': 2342,
            },
            {
                'feature_name2': 'test_string_val'
            }
        ]
        test_returned_dict = {
            'features_values': {
                'feature_name1': 2342,
                'feature_name2': 'test_string_val'
            },
            'features_values_schema': {
                'fields': [
                    {
                        'required': True,
                        'type': "input",
                        'label': 'feature_name1',
                        'model': 'feature_name1',
                        'inputType': 'number'
                    },
                    {
                        'required': True,
                        'type': "input",
                        'label': 'feature_name2',
                        'model': 'feature_name2',
                        'inputType': 'text'
                    }
                ]
            }
        }
        self.maxDiff = None
        mock_obj = Mock()
        mock_obj.get_model_training_feature_list = Mock(
            return_value=test_feature_values)
        with patch('fyp_web_ml_project.route_handlers.mlmodels.ml_ops', new=mock_obj):
            returned_dict = mlmodels.get_prediction_factors_form_from_model(
                'test_name')

        mock_obj.get_model_training_feature_list.assert_called_once_with('test_name')
        self.assertEqual(returned_dict, test_returned_dict,
                         "Returned dict doesn't match")

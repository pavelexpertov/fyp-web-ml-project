import unittest
from unittest.mock import patch, Mock

import fyp_web_ml_project.ml_ops as ml_ops


class TestGetMlClassAndSettingsListFunction(unittest.TestCase):

    def setUp(self):
        self.test_property_key_dict_1 = {'key1': 234234, 'key2': 'sdfsdf'}
        self.test_property_key_dict_2 = {'key3': 52, 'key4': 'hel'}
        mock_test1 = Mock()
        mock_test1().get_current_settings_parameters = Mock(return_value=self.test_property_key_dict_1)
        self.mock_test1 = mock_test1
        mock_test2 = Mock()
        mock_test2().get_current_settings_parameters = Mock(return_value=self.test_property_key_dict_2)
        self.mock_test2 = mock_test2
        self.class_objects_dict = {'test1': mock_test1, 'test2': mock_test2}
        self.test_list_comparison = [['test1', self.test_property_key_dict_1], ['test2', self.test_property_key_dict_2]]

    #@patch('fyp_web_ml_project.ml_ops.ml_class_dict', new=self.class_objects_dict)
    def test_getting_list_successfully(self):
        '''Tests whether function returns a list with values successfully'''
        #with patch.dict('fyp_web_ml_project.ml_ops.ml_class_dict', values=self.class_objects_dict, clear=True):
            #self.assertEqual(ml_ops.ml_class_dict, self.class_objects_dict, "mock objects in class and mocked module are not equal to each other")
        with patch.dict('fyp_web_ml_project.ml_ops.ml_class_dict', values=self.class_objects_dict, clear=True):
            class_and_settings_list = ml_ops.get_ml_class_and_settings_list()
        self.mock_test1().get_current_settings_parameters.assert_called_with()
        self.mock_test2().get_current_settings_parameters.assert_called_with()
        for coll in self.test_list_comparison:
            self.assertIn(coll, class_and_settings_list, "An collected item doesn't match")





if __name__ == '__main__':
    unittest.main()

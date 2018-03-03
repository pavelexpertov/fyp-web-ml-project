import unittest
from unittest.mock import patch, Mock

import fyp_web_ml_project.ml_ops as ml_ops

class TestAddNewMlClassFunction(unittest.TestCase):

    def tearDown(self):
        '''Clearing out class instances at the end of the test'''
        ml_ops.ml_class_dict.clear()

    def test_successful_class_addition(self):
        '''Test successful addition of the class to the dictionary'''
        test_object = Mock()
        test_name = 'Test'
        ml_ops.add_new_ml_class(test_name, test_object)

    def test_duplicate_ml_class_name_exception_error(self):
        '''Test for duplicat ml class name exception'''
        test_object = Mock()
        test_name = 'Test'
        ml_ops.add_new_ml_class(test_name, test_object)
        with self.assertRaises(ml_ops.DuplicateMlClassName) as cm:
            ml_ops.add_new_ml_class(test_name, test_object)


if __name__ == '__main__':
    unittest.main()

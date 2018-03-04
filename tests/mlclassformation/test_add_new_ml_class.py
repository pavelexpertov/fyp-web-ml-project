import unittest
from unittest.mock import Mock, patch

import fyp_web_ml_project.ml_class_formation as ml_class_formation
from fyp_web_ml_project.ml_ops import ml_class_dict


class TestAddNewMlClassFunction(unittest.TestCase):
    def tearDown(self):
        '''Emptying ml_class_dict'''
        ml_class_dict.clear()

    def test_for_name_error_exception(self):
        '''Test for a NameError based exception'''
        test_code = "sadfasdffasd"
        with self.assertRaises(ml_class_formation.ClassSyntaxError) as exc:
            ml_class_formation.add_new_ml_class('test', test_code)

    def test_for_typeerror_error_exception(self):
        '''Test for a TypeError based exception'''
        test_code = "x = '23' + 23"
        with self.assertRaises(ml_class_formation.ClassSyntaxError) as exc:
            ml_class_formation.add_new_ml_class('test', test_code)

    def test_for_indentation_error_exception(self):
        '''Test for IndentationError exception'''
        test_code = '''
        class Test:
            def __init__(self):
                self.message = 'test'
        '''
        with self.assertRaises(ml_class_formation.ClassSyntaxError) as exc:
            ml_class_formation.add_new_ml_class('Test', test_code)

    def test_for_misnamed_parent_class_error_exception(self):
        '''Test for Misnamed Parent class exception'''
        test_text = '''
class Test(AbstractMlCls):
    def __init__(self):
        # super().__init__('Hi', 'just a random object')
        self.message = "Hello, I guess this is working"
'''
        with patch('fyp_web_ml_project.ml_ops') as mock_obj:
            with self.assertRaises(ml_class_formation.ClassSyntaxError) as cm:
                ml_class_formation.add_new_ml_class('Test', test_text)


    def test_for_simple_class(self):
        '''Test for a simple class creation'''
        test_code = '''
class Test:
    def __init__(self, name):
        self.name = name
'''
        with patch('fyp_web_ml_project.ml_ops') as mock_obj:
            ml_class_formation.add_new_ml_class('Test', test_code)

        # mock_obj.add_new_ml_class.assert_called_with('Test', )

    def test_for_inherited_class(self):
        '''Test for a simple class creation'''
        test_code = '''
class Test(AbstractMlClass):
    def __init__(self, name):
        self.name = name
'''
        with patch('fyp_web_ml_project.ml_ops') as mock_obj:
            ml_class_formation.add_new_ml_class('Test', test_code)

        # mock_obj.add_new_ml_class.assert_called_with('Test', )

    def test_for_successful_sci_kit_import(self):
        '''Test for a successful import of sci kit'''
        test_code = '''
import sklearn

class Test(AbstractMlClass):
    def __init__(self, name):
        self.name = name
'''
        with patch('fyp_web_ml_project.ml_ops') as mock_obj:
            ml_class_formation.add_new_ml_class('Test', test_code)


if __name__ == '__main__':
    unittest.main()

import unittest

import fyp_web_ml_project.ml_class_formation as ml_class_formation


class TestAddNewMlClassFunction(unittest.TestCase):

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
            ml_class_formation.add_new_ml_class('test', test_code)

    def test_for_simple_class(self):
        '''Test for a simple class creation'''
        test_code = '''
class Test:
    def __init__(self):
        self.message = 'test'
'''
        ml_class_formation.add_new_ml_class('test', test_code)

if __name__ == '__main__':
    unittest.main()

import unittest

import fyp_web_ml_project.json_form_utils as json_form_utils


class TestCreateJsonSchemaFieldFunction(unittest.TestCase):
    def setUp(self):
        # Creating a field for an text type input with required
        self.test_doc1 = {'name': 'test_name', 'value': 'string_test'}
        self.test_doc1_result = {
            'required': True,
            'type': 'input',
            'label': self.test_doc1['name'],
            'model': self.test_doc1['name'],
            'inputType': 'text'
        }
        # Creating a field for an integer type input with required
        self.test_doc2 = {'name': 'test_name', 'value': 23}
        self.test_doc2_result = {
            'required': True,
            'type': 'input',
            'label': self.test_doc2['name'],
            'model': self.test_doc2['name'],
            'inputType': 'number'
        }
        # Creating a field for an float type input with required
        self.test_doc3 = {'name': 'test_name', 'value': 23.342}
        self.test_doc3_result = {
            'required': True,
            'type': 'input',
            'label': self.test_doc3['name'],
            'model': self.test_doc3['name'],
            'inputType': 'number'
        }
        # Creating a field for an text type input without required
        self.test_doc4 = {'name': 'test_name', 'value': 'string_test'}
        self.test_doc4_result = {
            'required': False,
            'type': 'input',
            'label': self.test_doc4['name'],
            'model': self.test_doc4['name'],
            'inputType': 'text'
        }

        # Creating a field for an None type input
        self.test_doc5 = {'name': 'test_name', 'value': None}
        self.test_doc5_result = {
            'required': True,
            'type': 'input',
            'label': self.test_doc5['name'],
            'model': self.test_doc5['name'],
        }

    def test_with_string_type(self):
        '''Creating a field for an text type input with required'''
        d = self.test_doc1
        returned_dict = json_form_utils.create_json_schema_field(
            d['name'], d['value'])
        self.assertEqual(returned_dict, self.test_doc1_result,
                         "The returned generated schema field doesn't match")

    def test_with_integer_type(self):
        '''Creating a field for an integer type input with required'''
        d = self.test_doc2
        returned_dict = json_form_utils.create_json_schema_field(
            d['name'], d['value'])
        self.assertEqual(returned_dict, self.test_doc2_result,
                         "The returned generated schema field doesn't match")

    def test_with_float_type(self):
        '''Creating a field for an float type input with required'''
        d = self.test_doc3
        returned_dict = json_form_utils.create_json_schema_field(
            d['name'], d['value'])
        self.assertEqual(returned_dict, self.test_doc3_result,
                         "The returned generated schema field doesn't match")

    def test_with_string_type_without_required(self):
        '''Creating a field for a text type input without required'''
        d = self.test_doc4
        returned_dict = json_form_utils.create_json_schema_field(
            d['name'], d['value'], False)
        self.assertEqual(returned_dict, self.test_doc4_result,
                         "The returned generated schema field doesn't match")

    def test_with_none_type_without_required(self):
        '''Creating a field for a None type input'''
        d = self.test_doc5
        returned_dict = json_form_utils.create_json_schema_field(
            d['name'], d['value'])
        self.assertEqual(returned_dict, self.test_doc5_result,
                         "The returned generated schema field doesn't match")

    def test_with_bool_type(self):
        '''Creating a field for an None type input'''
        test_doc = {'name': 'test_name', 'value': True}
        test_doc_result = {
            'required': True,
            'type': 'checkbox',
            'label': test_doc['name'],
            'model': test_doc['name'],
        }
        d = test_doc
        returned_dict = json_form_utils.create_json_schema_field(
            d['name'], d['value'])
        self.assertEqual(returned_dict, test_doc_result,
                         "The returned generated schema field doesn't match")

    def test_raising_exception(self):
        '''Test for raising an exception when there's unknown type'''
        with self.assertRaises(json_form_utils.UnrecognisedTypeError) as cm:
            json_form_utils.create_json_schema_field(
                'test_field', ['test_value'])

        exc = cm.exception
        expected_err_msg = "Unrecognised Type -- FieldName: test_field, Value: ['test_value'], Its Type: <class 'list'>"
        self.assertEqual(expected_err_msg, str(
            exc), "Error messages don't match")


if __name__ == '__main__':
    unittest.main()

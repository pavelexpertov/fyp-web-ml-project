import unittest
import fyp_web_ml_project.validator_utils as validator_utils


class TestCheckQueryJson(unittest.TestCase):

    def setUp(self):
        self.test_function = validator_utils.check_query_json
        self.normal_test_query_json = {'features_list': [
        ], 'start_date': '2010-05-05', 'end_date': '2011-07-21', 'store_number': 23}
        self.five_keys_query_json = {'extra_key': 23, 'features_list': [
        ], 'start_date': '2010-05-05', 'end_date': '2011-07-21', 'store_number': 23}
        self.three_keys_query_json = {
            'start_date': '2010-05-05', 'end_date': '2011-07-21', 'store_number': 23}
        self.incorrect_test_query_json = {'test_list': [
        ], 'start_date': '2010-05-05', 'end_date': '2011-07-21', 'store_number': 23}

    def test_successful_validation(self):
        '''Tests whether the function runs silently'''
        self.test_function(self.normal_test_query_json)

    def test_more_keys_json(self):
        '''Tests when a json has more than four keys'''
        with self.assertRaises(Exception) as cm:
            self.test_function(self.five_keys_query_json)

        self.assertEqual(str(cm.exception), "There's supposed to be 4 keys rather than 5")


    def test_less_keys_json(self):
        '''Tests when a json has less than four keys'''
        with self.assertRaises(Exception) as cm:
            self.test_function(self.three_keys_query_json)

        self.assertEqual(str(cm.exception), "There's supposed to be 4 keys rather than 3")


    def test_wrong_keys_json(self):
        '''Tests when a json has wrongly named keys'''
        with self.assertRaises(Exception) as cm:
            self.test_function(self.incorrect_test_query_json)

        self.assertEqual(str(cm.exception), "A query key doesn't exist in the json: features_list")


if __name__ == '__main__':
    unittest.main()

# Purpose of the script is to test creating a class from text and
# getting an instance from a local space and not to mentin to check
# that it can see the abstract class in namespace

from fyp_web_ml_project.ml_class_formation import add_new_ml_class
from fyp_web_ml_project.ml_ops import ml_class_dict

# test_text = '''
# class Test:
    # def __init__(self):
        # self.message = "Hello hahaah"
# '''

test_text = '''
class Test(AbstractMlClass):
    def __init__(self):
        super().__init__('Hi', 'just a random object')
        self.message = "Hello, I guess this is working"
'''

add_new_ml_class('Test', test_text)
for key, item in ml_class_dict.items():
    print(key, item)
instan = ml_class_dict['Test']
print("Here's the class", instan)
i = instan()
print("And here's an instance's message the message:", i.message)

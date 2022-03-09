# Lesson 14 - Testing you Code
# Unit tests checks one aspect of a functions behavior. For each test needing
# to be done on a function call, will require a new unit test.

# A test case is a collection of unit tests to ensure a function is tested on
# many situations. Test cases are made up of a class that import the unittest
# module and subclasses the unittest.TestCase class

import unittest
from house import House


# define a function that can be tested
def get_make_model(make, model):
    vehicle_type = '{0} {1}'.format(make, model)
    return vehicle_type


class SampleTesting(unittest.TestCase):
    # positive passing test
    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')

    # negative failing test
    def test_lower(self):
        self.assertEqual('hello'.lower(), 'Hello')

    # testing above function
    def test_make_model(self):
        formatted = get_make_model('Chevy', 'Silverado')
        self.assertEqual(formatted, 'Chevy Silverado')


class TestHouse(unittest.TestCase):
    def setUp(self):
        self.house = House(20, 'concrete', 'steel', 'red')

    def test_door_color(self):
        self.assertEqual(self.house.door_color, 'blue')

    def test_door_open_close(self):
        self.assertIsNone(self.house.door_open_close())


if __name__ == '__main__':
    unittest.main()

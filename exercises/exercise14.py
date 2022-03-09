# Tests would not run whilst in functions even when function is called.
# Unittest doesn't seem to be able to read the Test class when it is placed
# inside of a function.

# Importing both of these here since unittest is used for all problems and
# the module is used for problem 1 and 2.
import unittest
from exercises.exercise14_modules.city_functions import get_city_country

# 1.On page 215 of your book, do 11-1 of the Try it Yourself. Put all your
# code in your exercise14.py file.
print('#1 Problem')
# 11-1. City, Country: Write a function that accepts two parameters: a city
# name and a country name. The function should return a single string of the
# form City, Country, such as Santiago, Chile. Store the function in a module
# called city_functions.py.
# - Create a file called test_cities.py that tests the function you just wrote
#  (remember that you need to import unittest and the function you want to
#  test). Write a method called test_city_country() to verify that calling
#  your function with values such as 'santiago' and 'chile' results in the
#  correct string. Run test_cities.py, and make sure test_city_country() passes.
print('11.1 City, Country')


class TestCity(unittest.TestCase):
    """Unit test for get_city_country"""
    def test_output(self):
        capital = get_city_country('Washington DC', 'United States')
        self.assertEqual(capital, 'Washington DC, United States')


print('\n')


# 2.On page 216 of your book, do 11-2 of the Try it Yourself. Put all your
# code in your exercise14.py file.
print('#2 Problem')
# 11-2. Population: Modify your function so it requires a third parameter,
# population. It should now return a single string of the form City, Country
# – population xxx, such as Santiago, Chile – population 5000000. Run
# test_cities.py again. Make sure test_city_country() fails this time.
# - Modify the function so the population parameter is optional. Run
#   test_cities.py again, and make sure test_city_country() passes again.
# - Write a second test called test_city_country_population() that verifies you
#   can call your function with the values 'santiago', 'chile',
#   and 'population=5000000'. Run test_cities.py again, and make sure this new
#   test passes.
print('11.2 Population')
# Already imported p


class TestCityPopulation(unittest.TestCase):
    """Unit test for get_city_country for population"""
    def test_output_population(self):
        capital = get_city_country('Washington DC', 'United States', '500,000')
        self.assertEqual(capital,
                         'Washington DC, United States - population: 500,000')


print('\n')


# 3.On page 221 of your book, do 11-3 of the Try it Yourself. Put all your
# code in your exercise14.py file.
print('#3 Problem')
# 11-3. Employee: Write a class called Employee. The __init__() method should
# take in a first name, a last name, and an annual salary, and store each of
# these as attributes. Write a method called give_raise() that adds $5,
# 000 to the annual salary by default but also accepts a different raise
# amount.
# - Write a test case for Employee. Write two test methods,
#   test_give_default_raise() and test_give_custom_raise(). Use the setUp()
#   method so you don’t have to create a new employee instance in each test
#   method. Run your test case, and make sure both tests pass.


class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, rais=5_000):
        """Raises annual salary"""
        self.annual_salary = int(self.annual_salary) + rais
        return self.annual_salary


class TestEmployee(unittest.TestCase):
    """Tests Employee Class"""

    def setUp(self):
        """Sets up an employee to test"""
        self.employee = Employee('Larry', 'King', 50_000)

    def test_default_raise(self):
        """Unit Test for default raise"""
        self.assertEqual(self.employee.give_raise(), 55_000)

    def test_give_custom_raise(self):
        """Unit test for custom raise"""
        self.assertEqual(self.employee.give_raise(3_000), 53_000)


# Keeping this at the bottom so all code will run fine.
if __name__ == '__main__':
    unittest.main()

# Write functions for 1 -3 below. Call the function to ensure the results are
# correct.
# 1.On page 173 of yourbook, do 9-6 of the Try it Yourself. Put all your code
# in your exercise11.py file.
print('#1 Problem')
# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
# Write a class called IceCreamStand that inherits from the Restaurant class
# you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either
# version of the class will work; just pick the one you like better. Add an
# attribute called flavors that stores a list of ice cream flavors. Write a
# method that displays these flavors. Create an instance of IceCreamStand,
# and call this method.
print('9.6 Ice Cream')


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name} serves {self.cuisine_type}.')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open.')


class IceCreamStand(Restaurant):

    # Using * for flavors so list is stored inside of object rather than
    # outside of object that is passed through an argument. This seemed more
    # in line with the instructions.
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self._flavors = [*flavors]

    def display_flavors(self):
        print(f'{self.restaurant_name} flavors:')
        for flavor in self._flavors:
            print(f'- {flavor}')


yolo_ice_cream = IceCreamStand('Yolo Ice Cream', 'Ice Cream', 'Chocolate',
                               'Vanilla', 'Mint', 'YOLO')

yolo_ice_cream.display_flavors()


print('\n')


# 2.On page 173 of your book, do 9-7 of the Try it Yourself. Put all your
# code in your exercise11.py file.
print('#2 Problem')
# 9-7. Admin: An administrator is a special kind of user. Write a class
# called Admin that inherits from the User class you wrote in Exercise 9-3 (
# page 162) or Exercise 9-5 (page 167). Add an attribute, privileges,
# that stores a list of strings like "can add post", "can delete post",
# "can ban user", and so on. Write a method called show_privileges()that
# lists the administrator’s set of privileges. Create an instance of Admin,
# and call your method
print('9.7 Admin')


class User:
    def __init__(self, first_name, last_name, age, location, eye_color,
                 lifepoints):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.eye_color = eye_color
        self.lifepoints = lifepoints

    def describe_user(self):
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'Age: {self.age}')
        print(f'Location: {self.location}')
        print(f'Eye Color: {self.eye_color}')
        print(f'Lifepoints: {self.lifepoints}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}, welcome to the meta.')
        print()


class Admin(User):
    def __init__(self, first_name, last_name, age, location, eye_color,
                 lifepoints, *privileges):
        super().__init__(first_name, last_name, age, location, eye_color,
                         lifepoints)
        self.privileges = [*privileges]

    def show_privileges(self):
        print(f'{self.first_name} privileges:')
        for privilege in self.privileges:
            print(f'- {privilege}')


admin = Admin('Admin', 'Admin', 'Infinite', 'Everywhere', 'Black',
              'Infinite', 'Can ban users', 'Can mute.', 'Can delete posts')

admin.show_privileges()


print('\n')


# 3.On page 173 of your book, do 9-8 of the Try it Yourself. Put all your
# code in your exercise11.py file.
print('#3 Problem')
# 9-8. Privileges: Write a separate Privileges class. The class should have
# one attribute, privileges, that stores a list of strings as described in
# Exercise 9-7. Move the show_privileges() method to this class. Make a
# Privileges instance as an attribute in the Admin class. Create a new
# instance of Admin and use your method to show its privileges.
print('9.8 Privileges')


class Privileges:

    def __init__(self, *privileges):
        self.privileges = [*privileges]

    def show_privileges(self):
        print('Admin Privileges:')
        for privilege in self.privileges:
            print(f'- {privilege}')


# Overwriting Admin class for this problem.
class Admin(User):
    def __init__(self, first_name, last_name, age, location, eye_color,
                 lifepoints):
        super().__init__(first_name, last_name, age, location, eye_color,
                         lifepoints)
        self.privileges = Privileges('Can ban users', 'Can mute.',
                                     'Can delete posts')


admin = Admin('Admin', 'Admin', 'Infinite', 'Everywhere', 'Black', 'Infinite')
admin.privileges.show_privileges()


print('\n')


# 4.Using your Horse Objects from the Encapsulation exercise, create your 2
# child objects from the OOP section of the previous class. Use the property
# decorator for your child objects. Put both children objects inside your
# horse.py file.
print('#4 Problem')
print('''See child section of:
https://github.com/Newberrye/python-fundamentals/blob/main/exercises/horse.py
''')


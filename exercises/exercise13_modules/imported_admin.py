"""Module for storing User, Admin, and Priveleges Classes"""


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


class Privileges:

    def __init__(self, *privileges):
        self.privileges = [*privileges]

    def show_privileges(self):
        print('Admin Privileges:')
        for privilege in self.privileges:
            print(f'- {privilege}')


class Admin(User):
    def __init__(self, first_name, last_name, age, location, eye_color,
                 lifepoints):
        super().__init__(first_name, last_name, age, location, eye_color,
                         lifepoints)
        self.privileges = Privileges('Can ban users', 'Can mute.',
                                     'Can delete posts')


"""Module for exercise13 9.12 for storing Admin and Privileges Classes"""
from exercises.exercise13_modules.user import User


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

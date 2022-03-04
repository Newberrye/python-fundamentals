# Problem #3 says exercises 9.1 to 9.11 but the page only has uo to 9.3. I'm
# assuming that was a typo.

# Write functions for each of the items below. Call the function to ensure
# the results are correct.

# 1.On page 137 of your book, do 8-3 through 8-5 of the Try it Yourself. Put
# all your code in your exercise9.py file.
print('#1 Problem')
# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and
# the text of a message that should be printed on the shirt. The function
# should print a sentence summarizing the size of the shirt and the message
# printed on it.
# - Call the function once using positional arguments to make a
#   shirt.
# - Call the function a second time using keyword arguments.
print('8.3 T-Shirt')


def make_shirt(size, text):
    print(f'Shirt Size: {size}\nShirt Text: {text}\n')


# positional
make_shirt(10, 'Hello World')
# keywords
make_shirt(text='Hello World', size=10)

print()
# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are
# large by default with a message that reads I love Python. Make a large
# shirt and a medium shirt with the default message, and a shirt of any size
# with a different message.
print('8.4 Large Shirts')


def make_shirt(size='large', text='I love Python'):
    print(f'Shirt Size: {size.title()}\nShirt Text: {text.title()}\n')


# Large shirt and medium shirt. Not using keyword for second function since
# first parameter is size.
make_shirt()
make_shirt('medium')

# Any size, different message
make_shirt(text='I despise Python!')

print()
# 8-5. Cities: Write a function called describe_city() that accepts the name
# of a city and its country. The function should print a simple sentence,
# such as Reykjavik is in Iceland. Give the parameter for the country a
# default value. Call your function for three different cities, at least one
# of which is not in the default country.
print('8.5 Cities')


def describe_city(city, country='United States'):
    print(f'{city.title()} is in {country.title()}.')


describe_city('Wichita')
describe_city('Tulsa')
describe_city('paris', 'france')

print('\n')
# 2.On page 146 of your book, do 8-9 through 8-11 of the Try it Yourself. Put
# all your code in your exercise9.py file.
print('#2 Problem')
# 8-9. Messages: Make a list containing a series of short text messages. Pass
# the list to a function called show_messages(), which prints each text message
print('8.9 Messages')
messages_list = ['lol', 'xD', 'Radical!', 'Groovy', 'Do a barrel roll']


def print_messages(texts):
    for text in texts:
        print(text)


print_messages(messages_list)

print()
# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-
# 9. Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.
print('8.10 Sending Messages')


def send_messages(texts):
    new_list = []

    # For loop does not handle deleting from list during list, so a while loop
    # was used to get individual texts out instead.
    while texts:
        print(texts[0])
        new_list.append(texts[0])
        texts.pop(0)

    return new_list


sent_list = send_messages(messages_list)
print(messages_list)
print(sent_list)

print()
# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling
# the function, print both of your lists to show that the original list has
# retained its messages.
print('8.11 Archived Messages')
copied_list = send_messages(sent_list.copy())
print(copied_list)
print(sent_list)

print('\n')
# 3.On page 162 of your book, do 9-1 through 9-3 of the Try it Yourself. Put
# all your code in your exercise9.py file.
print('#4 Problem')
# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a
# cuisine_type. Make a method called describe_restaurant() that prints these
# two pieces of information, and a method called open_restaurant() that
# prints a message indicating that the restaurant is open.
# - Make an instance called restaurant from your class. Print the two attributes
#   individually, and then call both methods.
print('9.1 Restaurant')


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name} serves {self.cuisine_type}.')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open.')


restaurant1 = Restaurant('Long John Silvers', 'fish')

print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

print()
# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create
# three different instances from the class, and call describe_restaurant()
# for each instance.
print('9.2 Three Restaurants')
restaurant2 = Restaurant('Wendy\'s', 'fast food')
restaurant3 = Restaurant('Orange Wasps', 'honeycakes')
restaurant4 = Restaurant('Krusty Krab', 'pizza')

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant4.describe_restaurant()

print()
# 9-3. Users: Make a class called User. Create two attributes called
# first_name and last_name, and then create several other attributes that are
# typically stored in a user profile. Make a method called describe_user()
# that prints a summary of the user’s information. Make another method called
# greet_user() that prints a personalized greeting to the user.
# - Create several instances representing different users, and call both methods
#   for each user.
print('9.3 Users')


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


user1 = User('John', 'Cena', '56', 'Earth', 'brown', '88')
user2 = User('Mark', 'Hamilton', '47', 'Jupiter', 'blue', '0')
user3 = User('The Great', 'Smith', '16', 'Earth', 'amber', '78')
user4 = User('Ash', 'Ketchum', '12?', 'Cerise Labs', 'black', '100')

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
user4.describe_user()
user4.greet_user()


print('\n')
# 4.On page 167 of your book, do 9-4 and 9-5 of the Try it Yourself. Put all
# your code in your exercise9.py file.
print('#5 Problem')
# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# - Add a method called set_number_served() that lets you set the number of
#   customers that have been served. Call this method with a new number and
#   print the value again.
# - Add a method called increment_number_served() that lets you increment the
#   number of customers who’ve been served. Call this method with any number
#   you like that could represent how many customers were served in, say, a day
#   of business.
print('9.4 Number Served')


class RestaurantProblemFive:

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f'{self.restaurant_name} serves {self.cuisine_type}.')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open.')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant5 = RestaurantProblemFive('Long John Silvers', 'fish', 10_567)
print(restaurant5.number_served)
restaurant5.number_served = 5_678
print(restaurant5.number_served)

restaurant5.set_number_served(7_999)
print(restaurant5.number_served)

restaurant5.increment_number_served(101)
print(restaurant5.number_served)

print()
# 9-5. Login Attempts: Add an attribute called login_attempts to your User class
# from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
# that increments the value of login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0.
# - Make an instance of the User class and call increment_login_attempts()
#   several times. Print the value of login_attempts to make sure it was
#   incremented properly, and then call reset_login_attempts(). Print
#   login_attempts again to make sure it was reset to 0.
print('9.5 Login Attempts')


class UserNext:
    # Set default login attempts to 0 because all new users should have 0.
    def __init__(self, first_name, last_name, age, location, eye_color,
                 lifepoints, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.eye_color = eye_color
        self.lifepoints = lifepoints
        self.login_attempts = login_attempts

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

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user5 = UserNext('John', 'Souls', '38', 'Demon Souls', 'black', '0')

user5.increment_login_attempts()
print(user5.login_attempts)
user5.increment_login_attempts()
print(user5.login_attempts)
user5.increment_login_attempts()
print(user5.login_attempts)

user5.reset_login_attempts()
print(user5.login_attempts)


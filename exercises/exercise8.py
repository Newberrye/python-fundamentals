# Write functions for each of the items below. Call the function to ensure
# the results are correct.

# 1.On page 89 of your book, do 5-8 &5-9 of the Try it Yourself. Put all your
# code in your exercise8.py file.
print('#1 Problem')
# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each
# user after they log in to a website. Loop through the list, and print a
# greeting to each user:
# - If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# - Otherwise, print a generic greeting, such as Hello Jaden, thank you for
# logging in again.
print('5.8 Hello Admin')


def hello_admin():
    usernames = ['xxDeStroyerxx', 'GirlGamer', 'JohnRobert', 'admin', 'Q']

    for name in usernames:
        if name == 'admin':
            print(f'{name} - Greetings commander, the ship is yours.')
        else:
            print(f'Hello {name}. A special deal awaits you in your inbox!')


hello_admin()
print()
# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users
# is not empty.
# - If the list is empty, print the message We need to find some users!
# - Remove all the usernames from your list, and make sure the correct
#   message is printed.
print('5.9 No Users')


def hello_admin_59():
    usernames = []

    if usernames:
        for name in usernames:
            if name == 'admin':
                print(f'{name} - Greetings commander, the ship is yours.')
            else:
                print(f'Hello {name}. A special deal awaits you in your inbox!')
    else:
        print('Oh dear, all your users appear to be missing.')


hello_admin_59()


print('\n')
# 2.On page 89 of your book, do 5-10 of the Try it Yourself. Put all your
# code in your exercise8.py file.
print('#2 Problem')
# 5-10. Checking Usernames: Do the following to create a program that
# simulates how websites ensure that everyone has a unique username.
# - Make a list of five or more usernames called current_users.
# - Make another list of five usernames called new_users. Make sure one or
#   two of the new usernames are also in the current_users list.
# - Loop through the new_users list to see if each new username has already
#   been used. If it has, print a message that the person will need to enter a
#   new username. If a username has not been used, print a message saying
#   that the username is available.
# - Make sure your comparison is case-insensitive. If 'John' has been used,
#   'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
#   current_users containing the lowercase versions of all existing users.)
print('5.10 Checking Usernames')


def check_username():
    current_users = ['xxDeStroyerxx', 'GirlGamer', 'JohnRobert', 'admin', 'Q']
    new_users = ['new_guy', 'owner', 'admin', 'Q', '1234567890']

    # Creates a new current_user list that is lowercase for testing against
    # new_user lower cased
    current_users_lower = [new.lower() for new in current_users]

    for user in new_users:
        if user.lower() in current_users_lower:
            print(f'{user} is taken, please enter a new user')
        else:
            print(f'{user} is available. You are UNIQUE!')


check_username()


print('\n')
# 3.On page 89 of your book, do 5-11 of the Try it Yourself. Put all your
# code in your exercise8.py file.
print('#3 Problem')
# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
# as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# - Store the numbers 1 through 9 in a list.
# - Loop through the list.
# - Use an if-elif-else chain inside the loop to print the proper ordinal ending
#   for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th
#   9th", and each result should be on a separate line
print('5.11 Ordinal Numbers')


def ordinal_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for number in numbers:
        if number == 1:
            print('1st')
        elif number == 2:
            print('2nd')
        elif number == 3:
            print('3rd')
        else:
            print(f'{number}th')


ordinal_numbers()


print('\n')
# 4.On page 99 of your book, do 6-1 of the Try it Yourself. Put all your code
# in your exercise8.py file.
print('#4 Problem')
# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city. Print
# each piece of information stored in your dictionary
print('6.1 Person')


def person():
    person_dict = {
        'first name': 'Phillip',
        'last_name': 'Jenkins',
        'age': 29,
        'city': 'Pittsburgh'
    }

    for key, value in person_dict.items():
        print(f'{key} is {value}')


person()


print('\n')
# 5.On page 112 of your book, do 6-7 of the Try it Yourself. Put all your
# code in your exercise8.py file.
print('#5 Problem')
# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
# Make two new dictionaries representing different people, and store all
# three dictionaries in a list called people. Loop through your list of
# people. As you loop through the list, print everything you know about each
# person.
print('6.7 People')


def peoples():
    person1 = {
        'first name': 'Phillip',
        'last_name': 'Jenkins',
        'age': 29,
        'city': 'Pittsburgh'
    }
    person2 = {
        'first name': 'Allen',
        'last_name': 'Reinhart',
        'age': 24,
        'city': 'Tulsa'
    }
    person3 = {
        'first name': 'George',
        'last_name': 'Washington',
        'age': 290,
        'city': 'Mount Vernon'
    }
    people = [person1, person2, person3]

    for pers in people:
        for key, value in pers.items():
            print(f'{key} is {value}')
        print()


peoples()

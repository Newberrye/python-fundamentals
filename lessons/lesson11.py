# Lesson 11 Inheritance & Polymorphism
# Inheritance in Python is about objects acquiring all the properties and
# behaviours of a parent object.
class Parent:
    # constructor
    def __init__(self, name, eye_color):
        self.name = name
        self.eye_color = eye_color

    def to_name(self):
        return self.name

    def my_eye_color(self):
        return self.eye_color

    def is_working(self):
        return True


class Child(Parent):

    def is_working(self):
        return False


# Parent
my_parent = Parent('Debbie', 'Brown')
print(my_parent.to_name())
print(my_parent.my_eye_color())
print(my_parent.is_working())

# Child
my_child = Child('David', 'Blue')
print(my_child.to_name())
print(my_child.my_eye_color())
print(my_child.is_working())


class SecondParent:
    def __init__(self, last_name, hair_color):
        self.last_name = last_name
        self.hair_color = hair_color

    def to_last(self):
        return self.last_name

    def is_working(self):
        return True


class SecondChild(Parent, SecondParent):
    def __init__(self, name, eye_color, last_name, hair_color):
        Parent.__init__(self, name, eye_color)
        SecondParent.__init__(self, last_name, hair_color)

    def is_working(self):
        return False


print()
# Second Parent
my_second_parent = SecondParent('Smith', 'Brown')
print(my_second_parent.to_last())
print(my_second_parent.is_working())

# Second Child that is of both parents.
my_second_parent = SecondChild('Mary', 'Brown', 'Smith', 'Blonde')
print(my_second_parent.hair_color)
print(my_second_parent.is_working())


# Polymorphism using 2 different classes
class Car:
    # constructor
    def __init__(self, model, color):
        self._model = model
        self._color = color

    def info(self):
        print(str.format('I like my {0} {1}', self._color, self._model))

    def move(self):
        print('My {0} rides fast on the road.'.format(self._model))


class Boat:
    def __init__(self, model, color):
        self._model = model
        self._color = color

    def info(self):
        print(str.format('I like my {0} {1}', self._color, self._model))

    def move(self):
        print('My {0} rides fast on the road.'.format(self._model))


car1 = Car('Camero', 'Green')
boat1 = Boat('Fishing Boat', 'Blue Metallic')

print()
for vehicle in (car1, boat1):
    vehicle.info()
    vehicle.move()
print()


# Polymorphism and Inheritance
class Animal:
    def __init__(self, family):
        self._family = family

    def info(self):
        pass

    def make_sound(self):
        return 'RUMBLE GOES THE {0}'.format(self._family)

    def __str__(self):
        return self._family


class Dog(Animal):
    def __init__(self, name):
        super().__init__('Canine')
        self._name = name

    def info(self):
        return 'My dog\'s name is {0} and he is a {1}'.format(self._name,
                                                              self._family)

    def make_sound(self):
        return 'barks'

    def __str__(self):
        return self._name


class Frog(Animal):
    def __init__(self, name):
        super().__init__('Amphibian')
        self._name = name

    def info(self):
        return 'My frog\'s name is {0} and he is a {1}'.format(self._name,
                                                               self._family)

    def __str__(self):
        return self._name


dog1 = Dog('Lucky')
frog1 = Frog('George')
print(dog1.info())
print(frog1.info())
print(dog1.make_sound())
print(frog1.make_sound())

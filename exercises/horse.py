# 3.In your horse.py file, write your horse object using your notes from the 
# Intro to Programming class. Refine your attributes for your constructor. 
# Utilize the @property decorator along with the attribute methods for each 
# of your variable attributes. Be sure to test your class and properties. 
# 2.In your watch.py file, write your watch object using your notes from the
# Intro to Programming class. Refine your attributes for your constructor.
# Utilize the property() along with the getter and setter for eachof your
# variable attributes. Be sure to test your class and properties.
class Horse:
    def __init__(self, horseshoed, size, color):
        self._horseshoed = horseshoed
        self._size = size
        self._color = color

    @property
    def horseshoed(self):
        return self._horseshoed

    @horseshoed.setter
    def horseshoed(self, horseshoed):
        self._horseshoed = horseshoed

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, sizing):
        self._size = sizing

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def gallop(self):
        print('The horse gallops.')


mustang = Horse('yes', 'large', 'brown')

print(mustang.horseshoed)
mustang.horseshoed = 'no'
print(mustang.horseshoed)
print()

print(mustang.size)
mustang.size = 'small'
print(mustang.size)
print()

print(mustang.color)
mustang.color = 'silver'
print(mustang.color)
print()

mustang.gallop()


# 4.Using your Horse Objects from the Encapsulation exercise, create your 2
# child objects from the OOP section of the previous class. Use the property
# decorator for your child objects. Put both children objects inside your
# horse.py file.
print('\n')
print('Exercise 11: #4 Problem: Horse Children')


class Pony(Horse):
    def __init__(self, horseshoed, size, color, age, height):
        super().__init__(horseshoed, size, color)
        self._age = age
        self._height = height

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, aging):
        self._age = aging

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def feed_pony(self):
        print('Feeds the pony.')


class Donkey(Horse):
    def __init__(self, horseshoed, size, color, teeth, tail_length):
        super().__init__(horseshoed, size, color)
        self._teeth = teeth
        self._tail_length = tail_length

    @property
    def teeth(self):
        return self._teeth

    @teeth.setter
    def teeth(self, teething):
        self._teeth = teething

    @property
    def tail_length(self):
        return self._tail_length

    @tail_length.setter
    def tail_length(self, tail_length):
        self._tail_length = tail_length

    def kick_your_butt(self):
        print('Donkey proceeds to kick your behind.')


pony = Pony('no', 'extra small', 'blue', '1 year old', '5 feet tall')
donkey = Donkey('yes', 'small', 'gray', 'large', 'stubby')

print(pony)
print(pony.horseshoed)
print(pony.height)
pony.feed_pony()
print()
print(donkey)
print(donkey.horseshoed)
print(donkey.tail_length)
donkey.kick_your_butt()

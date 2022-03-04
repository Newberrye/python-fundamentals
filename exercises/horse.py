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

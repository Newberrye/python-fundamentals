# 1.In your boat.py file, write your boat object using your notes from the
# Intro to Programming class. Refine your attributes for your constructor.
# Utilize the property() along with the getter and setter for each of your
# variable attributes. Be sure to test your class and properties.
class Boat:
    def __init__(self, paint, size, max_speed):
        self._paint = paint
        self._size = size
        self._max_speed = max_speed

    def get_paint(self):
        return self._paint

    def set_paint(self, color):
        self._paint = color

    def del_paint(self):
        del self._paint

    def get_size(self):
        return self._size

    def set_size(self, sizing):
        self._size = sizing

    def del_size(self):
        del self._size

    def get_max_speed(self):
        return self._max_speed

    def set_max_speed(self, speed):
        self._max_speed = speed

    def del_max_speed(self):
        del self._max_speed

    def turn_engine_on(self):
        print('The Engine was turned on.')

    paint = property(get_paint, set_paint, del_paint)
    sizing = property(get_size, set_size, del_size)
    max_speed = property(get_max_speed, set_max_speed, del_max_speed)


speed_boat = Boat('red', 'large', '20mph')

print(speed_boat.paint)
speed_boat.paint = 'blue'
print(speed_boat.paint)
print()

print(speed_boat.sizing)
speed_boat.sizing = 'small'
print(speed_boat.sizing)
print()

print(speed_boat.max_speed)
speed_boat.max_speed = '25mph'
print(speed_boat.max_speed)
print()

speed_boat.turn_engine_on()

# 2.In your watch.py file, write your watch object using your notes from the
# Intro to Programming class. Refine your attributes for your constructor.
# Utilize the property() along with the getter and setter for eachof your
# variable attributes. Be sure to test your class and properties.
class Watch:
    def __init__(self, size, display_time, weight):
        self._size = size
        self._display_time = display_time
        self._weight = weight

    def get_size(self):
        return self._size

    def set_size(self, sizing):
        self._size = sizing

    def del_size(self):
        del self._size

    def get_display_time(self):
        return self._display_time

    def set_display_time(self, time):
        self._display_time = time

    def del_display_time(self):
        del self._display_time

    def get_weight(self):
        return self._weight

    def set_weight(self, grams):
        self._weight = grams

    def del_weight(self):
        del self._weight

    def set_alarm(self):
        print('Alarm was set.')

    size = property(get_size, set_size, del_size)
    display_time = property(
        get_display_time, set_display_time, del_display_time
                            )
    weight = property(get_weight, set_weight, del_weight)


apple_watch = Watch('small', '3:45', '20grams')

print(apple_watch.size)
apple_watch.size = 'large'
print(apple_watch.size)
print()

print(apple_watch.display_time)
apple_watch.display_time = '4:58'
print(apple_watch.display_time)
print()

print(apple_watch.weight)
apple_watch.weight = '50grams'
print(apple_watch.weight)
print()

apple_watch.set_alarm()


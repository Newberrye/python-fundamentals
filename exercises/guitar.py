# 4.In your guitar.py file, write your guitar object using your notes from 
# the Intro to Programming class. Refine your attributes for your 
# constructor. Utilize the @property decorator along with the attribute 
# methods for each of your variable attributes. Be sure to test your class 
# and properties.
class Guitar:
    def __init__(self, number_of_strings, electrical, amp_port):
        self._number_of_strings = number_of_strings
        self._electrical = electrical
        self._amp_port = amp_port

    @property
    def number_of_strings(self):
        return self._number_of_strings

    @number_of_strings.setter
    def number_of_strings(self, number_of_strings):
        self._number_of_strings = number_of_strings

    @property
    def electrical(self):
        return self._electrical

    @electrical.setter
    def electrical(self, electric):
        self._electrical = electric

    @property
    def amp_port(self):
        return self._amp_port

    @amp_port.setter
    def amp_port(self, amp_port):
        self._amp_port = amp_port

    def play_instrument(self):
        print('You shred a tune with your intrument.')


electric_guitar = Guitar('6', 'electric', 'yes')

print(electric_guitar.number_of_strings)
electric_guitar.number_of_strings = '8'
print(electric_guitar.number_of_strings)
print()

print(electric_guitar.electrical)
electric_guitar.electrical = 'non-electric'
print(electric_guitar.electrical)
print()

print(electric_guitar.amp_port)
electric_guitar.amp_port = 'no'
print(electric_guitar.amp_port)
print()

electric_guitar.play_instrument()

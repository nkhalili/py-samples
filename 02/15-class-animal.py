class Animal:
    ## Class Variables, same for all objects of a class if they are mutable
    ## if you need a costant variable for your class, use immutable types
    x = [1, 2, 3]

    ## any special methods starts and ends with double underscores
    # def __init__(self, type, name, sound):
    def __init__(self, **kwargs):
        # Object Variables starts with underscore _ this means do not touch this! use setters instead.
        # python doesn't have private variables
        self._type = kwargs['type'] if 'type' in kwargs else '-'
        self._name = kwargs['name'] if 'name' in kwargs else '-'
        self._sound = kwargs['sound'] if 'sound' in kwargs else '-'

    ## getter
    def type(self):
        return self._type

    ## getter and setter
    def name(self, n=None):
        if n:
            self._name = n
        return self._name

    def sound(self):
        return self._sound

    #3 show method
    def show(self):
        print(
            f'Name: {self.name()}, Type: {self.type()}, Sound: {self.sound()}')

    ## special method str, overriding string conversion
    def __str__(self):
        # always read values using getters
        return f'Name: {self.name()}, Type: {self.type()}, Sound: {self.sound()}'


def main():
    # animal = Animal('fluffy', 'kitten', 'rwar')
    animal = Animal(name='fluffy', type='kitten', sound='rwar')
    animal.name('New fluffy')
    # animal.show()
    print(animal)

    animal2 = Animal()
    animal2.show()

    # Changing a Class Variable, affects all objects of that class
    animal.x[0] = 7
    print(f'animal: {animal.x}')
    print(f'animal2: {animal2.x}')

if __name__ == "__main__":
    main()

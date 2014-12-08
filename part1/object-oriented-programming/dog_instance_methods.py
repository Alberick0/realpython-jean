class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    specie = 'mammal'

    def description(self):
        return '{} is {} years old'.format(self.name, self.age)

    def bark(self, sound):
        return '{} says {}'.format(self.name, sound)

oso = Dog('Oso', 2)
print oso.description()
print oso.bark('Arrrggghhh')

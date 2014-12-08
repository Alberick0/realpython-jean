class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    species = 'mammal'

def get_biggest_number(*args):
    return max(args)

oso = Dog('Oso', 2)
lexus = Dog('Lexus', 1)
sonata = Dog('Sonata', 3)

print "The oldest dog is {}".format(get_biggest_number(oso.age, lexus.age, sonata.age))

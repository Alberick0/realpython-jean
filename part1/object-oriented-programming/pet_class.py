# Parent class
class Dog(object):

    # Class attribute
    species = 'mammals'
    is_hungry = True

    def eat(self):
        if self.is_hungry == False:
            self.is_hungry = True
        else:
            self.is_hungry = False

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# child class (inherits from Dog() class)
class RusellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# child class (inherits from Dog() class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# exercise 1 
class Pet():
    def __init__(self):
        self.tom = Dog('Tom', 6)
        self.mike = Dog('Mike', 7)
        self.larry = Dog('Larry', 9)
        self.dogs = [self.tom, self.mike, self.larry]

    def output(self):
        for dog in self.dogs:
            dog.eat()

        if dog.is_hungry == True:
            status = 'hungry'
        else:
            status =  'not hungry'

        return "I have {total} dogs. {tom.name} is {tom.age}. {larry.name} is {larry.age}. And they're all {tom.species}, of course. My dogs are {status}".format(total=len(self.dogs), tom=self.tom, larry=self.larry, status=status)


result = Pet()
print result.output()

class Animal(object):
    status = 'Healthy'
    hungry = True
    vaccines = []

    def __init__(self, name, age, race, origin):
        self.name = name
        self.age = age
        self.race = race

    def feed(self):
        if self.hungry == False:
            print "Not hungry"
        else:
            self.hungry = False
            print "Animal was fed"

    def vaccinate(self, vaccie):
        self.vaccines.append(vaccie)


class Horse(Animal):
    weight = None
    shape = None

    def get_shape(self):
        self.shape = int(raw_input("What's the animal shape: "))


class Cow(Animal):
    weight = None
    total_milk = 0

    def get_weight(self):
        self.weight = int(raw_input("What's the animal weight: "))


    def get_milk(self):
        self.today_milk = int(raw_input("How many litters of milk: "))
        self.total_milk += self.today_milk


class Pig(Animal):
    weight = None

    def get_weight(self):
        self.weight = int(raw_input("What's the animal weight: "))


oso = Animal('Oso', 2, 'Husky', 'Purchased')
porky = Pig('Porky', 3, 'some race', 'born')
vaca = Cow('Vaca', 5, 'some race', 'purchased')

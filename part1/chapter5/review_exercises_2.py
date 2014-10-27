weight = 0.2
animal = 'newt'

print weight, "is the weight of the", animal
print "{} is the weight of the {}".format(weight, animal)
print "{1} is the weight of the {0}".format(animal, weight)
print "{weight} is the weight of the {animal}".format(animal = 'ant', weight = 0.2)



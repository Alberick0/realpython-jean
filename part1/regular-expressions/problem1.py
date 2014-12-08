import re

validation = re.compile(r'[a-z0-9]+@[a-z]*[.]com|org|edu|net', re.IGNORECASE)

name = raw_input("What is your email: ")

while not validation.search(name):
    print "Please enter your email correctly!"
    name = raw_input("Please enter your name: ")

print "\nYour name is {}!".format(name)

from capitals import capitals_dict
import random


while True:
    state, capital = random.choice(capitals_dict.items())
    answer = raw_input('What is the capital of {}? --> '.format(state)).lower()

    if answer == 'exit':
        print 'The answer was "{}", Goodbye'.format(capital)
        break
    elif answer == capital.lower():
        print 'Correct'
        break

 


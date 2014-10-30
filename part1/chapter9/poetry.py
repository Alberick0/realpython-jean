import random

# 0 = nouns | 1 = verbs | 2 = adjectives | 3 = prepositions | 4 = Adverbs
types = [
    ['fossil', 'horse', 'aardvark', 'judge', 'chef', 'mango', 'extrovert', 'gorilla'],
    ['kicks', 'jingles', 'bounces', 'slurps', 'meows', 'explodes', 'curdles'],
    ['furry', 'balding', 'incredulous', 'fragant', 'exuberant', 'glistening'],
    ['against', 'after', 'into', 'beneath', 'upon', 'for', 'in', 'like', 'over', 'within'],
    ['curiously', 'extravagantly', 'tantalizingly', 'furiously', 'sensuously']
]

poem = [ [], [], [], [], [] ]
vowels = 'a, e i, o ,u'

# this adds a word to the list in the current position of i
def adder(i, amount):
    while len(poem[i]) < amount:
       word = random.choice(types[i])

       if poem[i].count(word) == 0:
           poem[i].append(word)


# main function of the program this assembles the poem
def makePoem():
    for i in range(len(types)):
        if i < 3:
            adder(i, 3)
        elif i == 3:
            adder(i, 2)
        else:
            adder(i, 1)

    if poem[2][0][0] in vowels:
        article = 'An'
    else:
        article = 'A'

    # this returns the assembled poem
    return '''
{1} {0[2][0]} {0[0][0]}

{1} {0[2][0]} {0[0][0]} {0[1][0]} {0[3][0]} the {0[2][1]} {0[0][1]}
{0[4][0]}, the {0[0][0]} {0[1][1]}
the {0[0][1]} {0[1][2]} {0[3][1]} a {0[2][1]} {0[0][2]}
'''.format(poem, article)

print makePoem()


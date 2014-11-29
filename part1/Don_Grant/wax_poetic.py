# imports the modules to use
import psycopg2
import random

# Open conneciton with the postgres database
db_connection = psycopg2.connect("dbname=wn2sql user=postgres host=localhost")
connection_cursor = db_connection.cursor()

# This lists will contain each word type within multiple sublists in one list 
# sublist type based on index 0 = nouns, 1 = verbs, 2 = adjectives, 3 = Adverbs 4 = prepositions
words_lists = [[],
               [],
               [],
               ['curiously', 'extravagantly', 'tantalizingly', 'furiously', 'sensuously'],
               ['against', 'after', 'into', 'beneath', 'upon', 'for', 'in', 'like', 'over', 'within']]

vowels = 'aeiou'

# This will get a random word from the postgres database based on the word_type
def get_word(word_type):
    statement = "SELECT word.lemma FROM word INNER JOIN sense ON word.wordno=sense.wordno INNER JOIN synset ON synset.synsetno=sense.synsetno INNER JOIN lexname ON lexname.lexno = synset.lexno WHERE description LIKE '%{}%' ORDER BY RANDOM() LIMIT 1;".format(word_type)
    connection_cursor.execute(statement)
    return connection_cursor.fetchone()[0]

# This validates that the word we are getting for the db is not repeated
def validate_word(word_type, word_list):
    word = get_word(word_type)
    while not word in words_lists[word_list]:
        words_lists[word_list].append(word)


# This will fill the lists aboves with random words from the db
def generate_word_lists():
    for word_list in range(len(words_lists) - 2):
        while len(words_lists[word_list]) < 10:
            if word_list == 0:
                validate_word('noun', word_list)
            elif word_list == 1:
                validate_word('verb', word_list)
            elif word_list == 2:
                validate_word('adjective', word_list)


# This appends to the poem a certain amount of words
def get_word_poem(poem, word_list, amount):
    while len(poem[word_list]) < amount:
        word = random.choice(words_lists[word_list])
        while not word in poem[word_list]:
            poem[word_list].append(word) 
    return poem


''' sublist type based on index 0 = nouns, 1 = verbs, 2 = adjectives, 3 = Adverbs
4 = prepositions'''
def generate_poem():
    poem = list()
    for word_list in range(len(words_lists)):
        poem.append(list())
        if word_list < 3:
            while len(poem[word_list]) < 3:
                get_word_poem(poem, word_list, 3)
        elif word_list == 3:
            while len(poem[word_list]) < 1:
                get_word_poem(poem, word_list, 1)
        else:
            while len(poem[word_list]) < 2:
                get_word_poem(poem, word_list, 2)

    if poem[2][0][0] in vowels:
        article = 'An'
    else:
        article = 'A'

    # this returns the assembled poem
    return '''
{0} {1[2][0]} {1[0][0]}

{0} {1[2][0]} {1[0][0]} {1[1][0]} {1[4][0]} the {1[2][1]} {1[0][1]}
{1[3][0]}, the {1[0][0]} {1[1][1]}
the {1[0][1]} {1[1][2]} {1[4][1]} a {1[2][2]} {1[0][2]}
'''.format(article, poem)


# Main section
def makePoem():
    generate_word_lists()
    return generate_poem()

print makePoem()

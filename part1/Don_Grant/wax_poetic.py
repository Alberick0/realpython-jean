# imports the modules to use
import psycopg2
import random

# Open connection with the postgres database
db_connection = psycopg2.connect("dbname=wn2sql user=postgres host=localhost")
connection_cursor = db_connection.cursor()

# Constants
NOUS = 0
VERBS = 1
ADJECTIVES = 2
ADVERBS = 3
PREPOSITIONS = 4

# This lists will contain each word type within multiple sublists in one list 
# sublist type based on index 0 = nouns, 1 = verbs, 2 = adjectives, 3 = Adverbs 4 = prepositions
words_lists = [[],
               [],
               [],
               [],
               ['against', 'after', 'into', 'beneath', 'upon', 'for', 'in', 'like', 'over', 'within']]

vowels = 'aeiou'

# This will get a random word from the postgres database based on the word_type
def get_word(word_type):
    statement = "SELECT word.lemma FROM word INNER JOIN sense ON word.wordno=sense.wordno INNER JOIN synset ON synset.synsetno=sense.synsetno INNER JOIN lexname ON lexname.lexno = synset.lexno WHERE description LIKE '%{word}%' ORDER BY RANDOM() LIMIT 1;".format(word=word_type)
    connection_cursor.execute(statement)
    return connection_cursor.fetchone()[0]

# This validates that the word we are getting for the db is not repeated
def validate_word(word_type, word_list):
    word = get_word(word_type)
    while not word in words_lists[word_list]:
        words_lists[word_list].append(word)


# This will fill the lists aboves with 10 random words from the db
def generate_word_lists():
    for word_list in range(len(words_lists) - 1):
        while len(words_lists[word_list]) < 10:
            if word_list == NOUS:
                validate_word('noun', word_list)
            elif word_list == VERBS:
                validate_word('verb', word_list)
            elif word_list == ADJECTIVES:
                validate_word('adjective', word_list)
            elif word_list == ADVERBS:
                validate_word('adverb', word_list)


# This appends to the poem a certain amount of words
def get_word_poem(poem, word_list, amount):
    while len(poem[word_list]) < amount:
        word = random.choice(words_lists[word_list])
        while not word in poem[word_list]:
            poem[word_list].append(word) 
    return poem


# This populates the lists that the poem will use with the amount of word need it
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
    return """
{article} {adjectives[0]} {nouns[0]}

{article} {adjectives[0]} {nouns[0]} {verbs[0]} {prepositions[0]} the {adjectives[1]} {nouns[1]}
{adverbs[0]}, the {nouns[0]} {verbs[1]}
the {nouns[1]} {verbs[2]} {prepositions[1]} a {adjectives[2]} {nouns[2]}
""".format(article=article,nouns=poem[0],verbs=poem[1],adjectives=poem[2],adverbs=poem[3],prepositions=poem[4])


# Main section
def makePoem():
    generate_word_lists()
    return generate_poem()

print makePoem()

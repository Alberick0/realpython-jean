from Tkinter import *
import tkFileDialog
import random
import os 


main_window_labels = {}
poem = {'nouns':[], 'verbs':[], 'adjectives':[], 'prepositions':[], 'adverbs':[]}
vowels = 'aeiou'


def add_word_poem(key, amount):
    while len(poem[key]) < amount:
        word = random.choice(main_window_labels[key])
        while not word in poem[key]:
            poem[key].append(word)


def make_poem():
    for key in poem:
        if key == 'nouns' or key == 'verbs' or key == 'adjectives':
            add_word_poem(key, 3)
        elif key == 'prepositions':
            add_word_poem(key, 2)
        else:
            add_word_poem(key, 1)

    if poem['adjectives'][0] in vowels:
        article = 'An'
    else:
        article = 'A'

    return """
{article} {adjectives[0]} {nouns[0]}

{article} {adjectives[0]} {nouns[0]} {verbs[0]} {prepositions[0]} the {adjectives[1]} {nouns[1]}
{adverbs[0]}, the {nouns[0]} {verbs[1]}
the {nouns[1]} {verbs[2]} {prepositions[1]} a {adjectives[2]} {nouns[2]}
""".format(article=article,nouns=poem['nouns'],verbs=poem['verbs'],adjectives=poem['adjectives'],adverbs=poem['adverbs'],prepositions=poem['prepositions'])


def error_amount(key):
    main_window_labels[key].delete(0, 100)
    main_window_labels[key].insert(0, 'Invalid entry')


def validate_words():
    main_window_labels['nouns'] = noun_entry
    main_window_labels['verbs'] = verb_entry
    main_window_labels['adjectives'] = adjective_entry
    main_window_labels['prepositions'] = preposition_entry
    main_window_labels['adverbs'] = adverb_entry

    validator = 0

    for key in main_window_labels:
        temp = main_window_labels[key].get().replace(' ','').split(',')
        for i in temp:
            if temp.count(i) > 1:
                main_window_labels[key].delete(0, 100)
                main_window_labels[key].insert(0, 'Words Must be Unique')
                return False

        if key is 'nouns' or key is 'verbs' or key is 'adjectives':
            if len(temp) < 3:
                error_amount(key)
            else:
                main_window_labels[key] = temp
                validator += 1
        elif key is 'prepositions':
            if len(temp) < 2:
                error_amount(key)
            else:
                main_window_labels[key] = temp
                validator += 1
        elif key is 'adverbs':
            if len(temp) < 1:
                error_amount(key)
            else:
                main_window_labels[key] = temp
                validator += 1

    if validator == 5:
        return True


def result_window():
    def save_poem():
        types = [("Text files", "*.txt")]
        file_name_output = tkFileDialog.asksaveasfilename(filetypes=types, defaultextension=".txt")
        with open(file_name_output, 'wb') as file_output:
            file_output.writelines(result_poem.cget("text"))

    if validate_words() == True:
        result_window = Tk()
        result_window.title("Your poem")

        result_frame = Frame(result_window)
        result_frame.grid(padx=10, pady=10)

        result_poem_header = Label(result_frame, text="Your Poem")
        result_poem_header.grid(row=1, column=1)

        result_poem = Label(result_frame)
        result_poem.grid(row=2, column=1)

        result_poem.config(text=make_poem())

        save_button = Button(result_frame, text="Save poem", command=save_poem)
        save_button.grid(row=3, column=1)


main_window = Tk()
main_window.title("Poem Generator")

main_frame = Frame()
main_frame.grid(padx=5, pady=5)

header_label = Label(main_frame, text="Fill the list belows, separate each word with commas", font="Arial")
header_label.grid(row=1, column=1, columnspan=4, pady=5)

noun_label = Label(main_frame, text="Nouns:")
noun_label.grid(row=2, column=1, sticky=E)
noun_entry = Entry(main_frame, width=23)
noun_entry.grid(row=2, column=2)
noun_entry.insert(0, "Insert at least 3 nouns")

verb_label = Label(main_frame, text="Verbs:")
verb_label.grid(row=3, column=1, sticky=E)
verb_entry = Entry(main_frame, width=23)
verb_entry.grid(row=3, column=2)
verb_entry.insert(0, "Insert at least 3 verbs")

adjective_label = Label(main_frame, text="Adjectives:")
adjective_label.grid(row=4, column=1, sticky=E)
adjective_entry = Entry(main_frame, width=23)
adjective_entry.grid(row=4, column=2)
adjective_entry.insert(0, "Insert at least 3 adjectives")

preposition_label = Label(main_frame, text="Prepositions:")
preposition_label.grid(row=5, column=1, sticky=E)
preposition_entry = Entry(main_frame, width=23)
preposition_entry.grid(row=5, column=2)
preposition_entry.insert(0, "Insert at least 2 prepositions")

adverb_label = Label(main_frame, text="Adverbs:")
adverb_label.grid(row=6, column=1, sticky=E)
adverb_entry = Entry(main_frame, width=23)
adverb_entry.grid(row=6, column=2)
adverb_entry.insert(0, "Insert at least 1 adverb")

create_button = Button(main_frame, text="Create Poem", command=result_window)
create_button.grid(row=7, column=1, columnspan=4, pady=5)

main_window.mainloop()

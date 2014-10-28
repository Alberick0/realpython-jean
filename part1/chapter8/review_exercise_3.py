word = raw_input('Please enter a word:')
if len(word) < 5:
    print("this word is less than five letters")
elif len(word) > 5:
    print("this word is more than five letters")
else:
    print('this word is equal to 5')


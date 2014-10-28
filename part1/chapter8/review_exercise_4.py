from __future__ import division

while True:
    user_input = raw_input("What's your input: ")
    if user_input == 'q' or user_input == 'Q':
        break
    
for i in range(1,51):
    if i % 3 == 0:
        continue
    else:
        print i


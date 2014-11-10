print '\n'

poem = open('poem.txt', 'r')
for line in poem.readlines():
    print line,
poem.close()

print '\n'

with open('poem.txt', 'r') as poem:
    for line in poem.readlines():
        print line,
    
print '\n'

with open('poem.txt', 'r') as poem, open('output.txt', 'w') as output:
    for line in poem.readlines():
        output.write(line)

print '\n'

with open('output.txt', 'a') as myAppend:
    newLine = ['\nThis is the new line that I"m adding']
    myAppend.writeline(newLine)

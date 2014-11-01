cats = 100
walks = 100
total = []

for w in range(1, walks + 1):
    for c in range(0, cats):
        if w == 1:
            if len(total) < cats:
                for i in range(cats):
                    total.append(i)

        else:
            if c % w == 0:
                if c in total:
                    total.remove(c)
                else:
                    total.append(c)

print total

'''
cats = 100
hats = dict([('with', [])])
walks = 100

for w in range(1, walks + 1):
    for c in range(0, cats):
        if w == 1:
            if len(hats['with']) < cats:
                for i in range(cats):
                    hats['with'].append(1)

        else:
            if c % w == 0:
                if hats['with'][c] == 0:
                    hats['with'][c] = 1
                else:
                    hats['with'][c] = 0

print hats['with'].count(1)
'''




def divider(num):
    for i in range(1, num + 1):
        if (num % i) == 0:
            print i, 'is a divisor of', num


num = int(raw_input('Enter a positive integer:'))
divider(num)


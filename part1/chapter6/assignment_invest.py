def invest(amount, rate, time):

    print "principal amount:", amount
    print "annual rate of return:", rate

    for i in range(1, time + 1):
        amount = amount + (amount * rate)
        print "year", str(i) + ":", "$"+ str(amount)

invest(100, 0.05, 8)
print "END"

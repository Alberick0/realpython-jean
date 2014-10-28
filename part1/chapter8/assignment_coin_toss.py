from random import randint

trial = 10
toss_tail = 0
toss_head = 0
head = 0
tail = 1

# head = 0 tail = 1

if randint(0,1) == 0:
    head += 1

    while(tail == 0):
        toss_tail += 1

        if randint(0,1) == 1:
            tail += 1

    print "The average tosses for tail were", toss_tail

else:
    tail += 1

    while(head == 0):
        toss_head += 1

        if randint(0,1) == 0:
            head += 1

    print "The average tosses for head were", toss_head

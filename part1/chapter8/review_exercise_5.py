while True:
    try:
        num = int(raw_input("Please type an intenger: "))
        print "The typed number is", num
        break
    except ValueError:
        print "You did not type an integer, try again"
        

#Calculates amount of cash and leftover cash

while True:
    x = int(input('Welcome. Please choose one of the following options:\nPress 1 to add up cash and find out how much should go in the envelope\nPress 0 to quit\n')) 
    if x == 1:
        hundred = int(input('How many $100 bills are there? '))
        twenty = int(input('How many $20 bills are there? '))
        ten = int(input('How many $10 bills are there? '))
        five = int(input('How many $5 bills are there? '))
        one = int(input('How many $1 bills are there? '))
        hundreds = hundred * 100
        twentys = twenty * 20
        tens = ten * 10
        fives = five * 5
        ones = one
        maths = hundreds + twentys + tens + fives + ones
        if maths > 200:
            leftovers = maths - 200
            print(f'\nYou need to put {leftovers} dollars in the envelope.\n')
        else:
            print(f'\nYou have {maths} dollars. There is no need to put any cash in the envelope.\n')
    
    elif x == 0:
        print('Goodbye.')
        break
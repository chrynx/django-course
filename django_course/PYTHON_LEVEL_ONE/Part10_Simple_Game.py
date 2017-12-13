###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

import random
digits = list(range(10))
random.shuffle(digits)
digits = digits[:3]
print digits

print('###########################')
print('###########################')
print('### WELCOME TO THE GAME ###')
print('# GUESS THE THREE NUMBERS #')
print('###########################')
match = False
while match == False:
    guess = input('Guess what the three numbers are')
    answer = str(guess)
    a = int(answer[0])
    b = int(answer[1])
    c = int(answer[2])
    if a == digits[0] and b == digits[1] and c == digits[2]:
        print('You have won the game')
        match = True
    elif a == digits[0] or b == digits[1] or c == digits[2]:
        print('You have matched a position')
    elif a in digits or b in digits or c in digits:
        print('You guessed a number but in the wrong position')
    else:
        print'No match'
print('Thanks for playing')

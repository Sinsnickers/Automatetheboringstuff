# this is random number guessing game
import random

print("Hello, whats your name?")
userName = input()
print("Well, " + userName +", I am thinking of a number between 1 and 20.")
secretNumber = random.randint(1,20)
attemps = 1
while(True):
    print("Take a guess.")
    userNumber = int(input())
    if (attemps==6):
        print("Sorry, the number i was thinking of was " + str(secretNumber))
        break
    else:
        if userNumber < secretNumber:
            print("My number is higher.")
        elif userNumber > secretNumber:
            print("My number is lower.")
        else:
            print("Well done, u guessed the right number in " + str(attemps) + " guesses.")
            break
        attemps = attemps + 1
    

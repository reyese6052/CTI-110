# Guess the secret number
# April 22, 2018
# CTI-110 P5HW2 - Random Number Guessing Game
# Evita Reyes
#

import random
n = random.randint(1, 100)
print('Can you guess the secret number?')

def main():
    guess = int(input("Enter a number from 1 to 100: "))
    while n != "guess":
        if guess < n:
            print ("Too low")
            guess = int(input("Enter a number from 1 to 100: "))
        elif guess > n:
            print ("Too high")
            guess = int(input("Enter a number from 1 to 100: "))
        else:
            print ("You've guessed the secret number!")
            break

main()
        

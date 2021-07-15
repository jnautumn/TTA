name = input("What's your name? ")
print("Well, " + name + ", I'm thinking of a number between 1 and 10")
import random
number = random.randint(1,10)
guess = input("Have a guess: ")
guess = int(guess)
if guess == number: 
      print("Correct!")
if guess != number:
    number= str(number)
    print("No, I was thinking of " + number)

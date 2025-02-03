import random

target = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    
    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")
        break

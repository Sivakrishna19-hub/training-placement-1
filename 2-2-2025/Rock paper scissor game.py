import random

choices = ["rock", "paper", "scissors"]
user = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(choices)

if user == computer:
    result = "It's a tie!"
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    result = "You win!"
else:
    result = "You lose!"

print(f"Computer chose {computer}. {result}")

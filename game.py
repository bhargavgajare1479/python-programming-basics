import random

choices = ["rock", "paper", "scissors"]

print("🎮 Rock, Paper, Scissors Game")
print("Type rock, paper, or scissors")

user = input("Your choice: ").lower()
computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("It's a Tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("🎉 You Win!")
else:
    print("❌ You Lose!")
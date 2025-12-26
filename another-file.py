import random

number = random.randint(1, 10)
attempts = 3

print("Guess the number between 1 and 10")
print("You have 3 attempts")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 Correct! You win!")
        break
    elif guess > number:
        print("Too high!")
    else:
        print("Too low!")

    attempts -= 1

if attempts == 0:
    print("❌ Game Over! The number was:", number)
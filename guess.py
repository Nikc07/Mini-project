import random

# Computer picks a random number
secret = random.randint(1, 100)

print("🎯 Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret:
        print("Too low! 📉")
    elif guess > secret:
        print("Too high! 📈")
    else:
        print("🎉 Correct! You guessed it!")
        break

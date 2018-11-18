import random

secretNum = random.randint(1, 10)
tries = 5
print("I am thinking of a number between 1 and 10. You have %d guesses left." %(tries))
guess = int(input("What's the number?"))


while tries > 1:
    tries -= 1
    if guess < secretNum:
        guess = int(input("%d is too low! You have %d guesses left. What's the number?" %(guess, tries)))
    elif guess > secretNum:
        guess = int(input("%d is too high! You have %d guesses left. What's the number?" %(guess, tries)))

if guess > secretNum:
    print ("%d is too high! You have 0 guesses left." %(guess))
elif guess < secretNum:
    print ("%d is too high! You have 0 guesses left." %(guess))

if guess == secretNum:
    print("Yes, you win!")
# Number guessing game
import random

low = int(input("Enter the lower bound:  "))
high = int(input("Enter the upper bound:   "))
att = int(input("Enter the number of attempts:  " ))

print("You have", att, "attemps to guess the number between", low, "and", high)

number = random.randint(low, high)
count = 0 # guess counter

while count < att:
    count += 1
    guess = int(input("Enter youe guess: "))
    if guess == number:
        print("Congratulations, you guessed the number in", count, "attempts!")
        break
    elif count >= att and guess != number:
        print("Sorry, you have used all ypur attempts. The number was", number)
    elif guess < number:
        print("Your guess is too low. Try again.")
    elif guess > number:
        print("Your guess is too high. Try again.")

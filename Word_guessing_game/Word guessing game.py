# Word guessing game 
import random

words = ["flower", "phone", "computer", "water", "paper", "notebook", "table", "lamp", "python"]
word = random.choice(words)

print("Guess the caracters in the word.")
print("The word has", len(word), "characters.")

guesses = ''
turns = 10

while turns > 0:
    failed = 0 #counter of failed guesses
    for char in word:
        if char in guesses:
            print(char, end = ' ')
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("Congratulation! You guessed the word:", word)
        break
    print()
    guess = input("Guess a character: ")
    guesses += guess        
    if guess not in word:
        turns -= 1
        print("Wrong! You have", turns, "turns left.")
        if turns == 0:
            print("You lose! The word was:", word)

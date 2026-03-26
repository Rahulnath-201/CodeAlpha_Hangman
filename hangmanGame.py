import random

words = ["apple", "tiger", "chair", "robot", "plant"]
word = random.choice(words)

guessed_letters = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

    if all(letter in guessed_letters for letter in word):
        print("🎉 You won! The word was:", word)
        break
else:
    print("❌ You lost! The word was:", word)
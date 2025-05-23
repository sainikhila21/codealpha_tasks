Hungama game:

import random

# List of words to choose from
word_list = ["python", "hangman", "challenge", "programming", "developer", "algorithm"]

# Select a random word
secret_word = random.choice(word_list)
guessed_letters = set()
correct_letters = set(secret_word)
max_attempts = 6
attempts = 0

print("🎮 Welcome to Hangman!")
print("_ " * len(secret_word))

# Game loop
while attempts < max_attempts and correct_letters != guessed_letters:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in correct_letters:
        print("✅ Good guess!")
    else:
        attempts += 1
        print(f"❌ Wrong guess! Attempts left: {max_attempts - attempts}")

    # Display current word progress
    display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
    print(" ".join(display_word))

# End of game
if correct_letters == guessed_letters:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game over! The word was:", secret_word)

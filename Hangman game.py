import random

def hangman():
    # List of words to guess
    words = ['python', 'java', 'kotlin', 'javascript', 'csharp', 'swift', 'typescript', 'c++', 'php', 'ruby']
    # Randomly choose a word from the list
    word = random.choice(words)
    # Set of letters in the word
    word_letters = set(word)
    # Alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Set of already guessed letters
    guessed = set()
    # List of guessed letters
    guessed_letters = []
    # Number of attempts remaining
    attempts = 10

    print("Welcome to Hangman! Guess the word:")

    # Main game loop
    while len(word_letters) > 0 and attempts > 0:
        # Create a printable version of the word
        printable = [letter if letter in guessed else '_' for letter in word]
        # Print the current state of the word
        print(' '.join(printable))
        # Print the number of attempts remaining
        print('Attempts Remaining: ', attempts)
        # Get the user's guess
        guess = input('Please guess a letter: ').lower()

        # If the letter has already been guessed
        if guess in guessed:
            print('You have already guessed that letter.')
        # If the letter is in the alphabet
        elif guess in alphabet:
            # Add the letter to the set of guessed letters
            guessed.add(guess)
            # Add the letter to the list of guessed letters
            guessed_letters.append(guess)
            # If the letter is in the word
            if guess in word_letters:
                # Remove the letter from the set of letters in the word
                word_letters.remove(guess)
            else:
                # Decrement the number of attempts remaining
                attempts -= 1
                # Print a message indicating that the letter is not in the word
                print('That letter is not in the word.')
        else:
            # Print a message indicating that the guess was invalid
            print('Invalid guess.')

    # If the user ran out of attempts
    if attempts == 0:
        # Print the word
        print(' '.join(word))
        # Print a message indicating that the user has run out of attempts
        print("You've run out of attempts. The word was:", word)
    else:
        # Print a message indicating that the user has guessed the word
        print('Congratulations! You guessed the word:', word)

if __name__ == "__main__":
    hangman()

import random
def hangman():
    words = ['python', 'java', 'kotlin', 'javascript', 'csharp', 'swift', 'typescript', 'cplusplus', 'php', 'ruby']
    word = random.choice(words)
    word_letters = set(word)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    guessed = set()
    guessed_letters = []
    attempts = 10

    print("Welcome to Hangman! Guess the word:")

    while len(word_letters) > 0 and attempts > 0:
        printable = [letter if letter in guessed else '_' for letter in word]
        print(' '.join(printable))
        print('Attempts Remaining: ', attempts)
        guess = input('Please guess a letter: ').lower()

        if guess in guessed:
            print('You have already guessed that letter.')
        elif guess in alphabet:
            guessed.add(guess)
            guessed_letters.append(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                attempts -= 1
                print('That letter is not in the word.')
        else:
            print('Invalid guess.')

    if attempts == 0:
        print(' '.join(word))
        print("You've run out of attempts. The word was:", word)
    else:
        print('Congratulations! You guessed the word:', word)

if __name__ == "__main__":
    hangman()

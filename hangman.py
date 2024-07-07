##HANGMAN GAME


import random  # Import the random module for generating random words

def choose_word():
    """Choose a random word from a predefined list."""
    words = ['numpy', 'pandas', 'matplotlib', 'requests', 'flask', 'django', 'tensorflow', 'keras', 'opencv', 'pytorch',
             'beautiful_soup', 'seaborn', 'jupyter', 'sqlalchemy', 'plotly', 'scipy']
    return random.choice(words)

def display_word(word, guessed_letters):
    """
    Display the word with correctly guessed letters and underscores for unguessed letters.

    Args:
        word (str): The word to be guessed.
        guessed_letters (list): List of letters guessed by the player.

    Returns:
        str: The word with guessed letters revealed and underscores for unguessed letters.
    """
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter  # Show the letter if guessed
        else:
            display += '_ '  # Show underscore if not guessed
    return display.strip()  # Strip trailing space from the display string

def hangman(name):
    """Main function to play the hangman game."""
    word = choose_word()  # Choose a random word
    guessed_letters = []  # List to store guessed letters
    incorrect_guesses = 0  # Counter for incorrect guesses
    max_guesses = 3 * len(word)  # Maximum allowed incorrect guesses
    
    # Welcome message and game rules
    print(f"\nHello, Good luck {name}!!! Enjoy Hangman.\n")
    print("______Rules_____\n")
    print("In this game you have to guess the random word from a list of frequently used Python libraries to win.\n")
    print("You are allowed a sufficient number of incorrect guesses.\n")

    while incorrect_guesses < max_guesses:
        print("\nWord:", display_word(word, guessed_letters))  # Display the word with guessed letters
        guess = input("Guess a letter: ").lower()  # Get user input for a letter guess

        # Validate the guess
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid alphabet.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)  # Add the guessed letter to the list of guessed letters
        
        # Check if the guess is correct
        if guess in word:
            print("Good guess!")
            # Check if all letters in the word have been guessed
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You win the game!! You guessed the word correctly :", word)
                break
        else:
            print("Oops! That letter is not in the word.")
            incorrect_guesses += 1
        
        print("Incorrect guesses left:", max_guesses - incorrect_guesses)
    
    else:
        # If the player runs out of guesses
        print("\nSorry, You ran out of guesses.")
        print("Better luck next time...")
        print("\n_____Game over!_____\n The word was:", word)

print("Welcome to hangman game.\nI hope you will enjoy this.")
name = input("Enter your name: ")  # Get player's name
hangman(name)  # Start the game

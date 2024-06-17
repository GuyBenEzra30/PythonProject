
def is_valid_input(Guess_Letter):
    """
    Checks if the input is an 'abc' letter.

    Parameters:
    Guess_Letter (str): The input to validate.

    Returns:
    bool: True, False.
    """
    return Guess_Letter.isalpha() and len(Guess_Letter) == 1

def check_valid_input(Guess_Letter, old_letters_guessed):
    """
    Checks if the input is an 'abc' letter not guessed before.

    Parameters:
    Guess_Letter (str): The input to validate.
    old_letters_guessed (list): List of letters guessed so far.

    Returns:
    bool: True, False.
    """
    return len(Guess_Letter) == 1 and Guess_Letter.isalpha() and Guess_Letter.lower() not in old_letters_guessed

def try_update_letter_guessed(Guess_Letter, old_letters_guessed):
    """
    Updates the list of guessed letters if the input is valid.

    Parameters:
    Guess_Letter (str): The letter guessed by the user.
    old_letters_guessed (list): List of letters guessed so far.

    Returns:
    bool: True, False.
    """
    if check_valid_input(Guess_Letter, old_letters_guessed):
        old_letters_guessed.append(Guess_Letter.lower())
        return True
    else:
        print('X')
        print(" -> ".join(sorted(old_letters_guessed)))
        return False

def show_hidden_word(GAME_WORD, old_letters_guessed):
    """
    Creates a string showing the letters of the secret word guessed correctly and underscores for others.

    Parameters:
    GAME_WORD (str): The secret word to guess.
    old_letters_guessed (list): List of letters guessed so far.

    Returns:
    str: A string that shows the secret word with correctly guessed letters and underscores.
    """
    result = ''
    for char in GAME_WORD:
        if char in old_letters_guessed:
            result += char
        else:
            result += '_'
    return ' '.join(result)

def check_win(secret_word, old_letters_guessed):
    """
    Checks if all letters in the secret word have been guessed.

    Parameters:
    secret_word (str): The secret word to guess.
    old_letters_guessed (list): List of letters guessed so far.

    Returns:
    bool: True, False.
    """
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True

def choose_word(file_path, index):
    """
    Chooses a word from a file based on the index.

    Parameters:
    file_path (str): Path to the file containing words.
    index (int): Index of the word to choose.

    Returns:
    str: The word chosen from the file based on the index.
    """
    with open(file_path, 'r') as file:
        words = file.read().split()
    return words[index - 1 % len(words)]

def print_welcome_screen():
    """
    Prints the welcome screen.
    """
    print("Welcome to the game Hangman")
    HANGMAN_ASCII_ART = ("""
    
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                          __/ |                      
                         |___/
    
    """)
    print(HANGMAN_ASCII_ART)
    print("6")
    

HANGMAN_PHOTOS = {
    0: """
    x-------x
    """,
    1: """
    x-------x
    |
    |
    |
    |
    |
    """,
    2: """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    3: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    4: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
}

def main():
    print_welcome_screen()
    
    # Where the user enter the file, index.
    file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    
    secret_word = choose_word(file_path, index)
    old_letters_guessed = []
    MAX_TRIES = 6
    num_of_tries = 0
    
    # Starts the game
    print("Let’s start!")
    print(HANGMAN_PHOTOS[num_of_tries])
    print(show_hidden_word(secret_word, old_letters_guessed)) # Print hidden word

    while num_of_tries < MAX_TRIES and not check_win(secret_word, old_letters_guessed):
        guess = input("Guess a letter: ").strip().lower() # Ask user for guess
        if try_update_letter_guessed(guess, old_letters_guessed):
            if guess not in secret_word:
                num_of_tries += 1
                print(":(")
            print(HANGMAN_PHOTOS[num_of_tries])
            print(show_hidden_word(secret_word, old_letters_guessed)) # Print updated hidden word
        else:
            print("Please try again, enter a letter for 'a - z' ")

    if check_win(secret_word, old_letters_guessed):
        print("WIN -> Good job, want to play again? run the program again!")
    else:
        print("LOSE -> the secret word was = ", secret_word)

    play_again = input("Do you want to play again? (y/n): ").strip().lower()

    if play_again == "y":
        main() # Restart the game if player wants to play again
    else:
        print("Hope you enjoyed the hangman game! See you soon!")
        return

if __name__ == "__main__":
    main()

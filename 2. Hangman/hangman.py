import random

# Game logic
def play_game():

    gameRunning = True
    words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
            'coyote crow deer dog donkey duck eagle ferret fox frog goat '
            'goose hawk lion lizard llama mole monkey moose mouse mule newt '
            'otter owl panda parrot pigeon python rabbit ram rat raven '
            'rhino salmon seal shark sheep skunk sloth snake spider '
            'stork swan tiger toad trout turkey turtle weasel whale wolf '
            'wombat zebra ').split()

    num = random.randint(0,len(words)-1)
    word = words[num]

    #Testing the word
    print("The word is: ", word)

    # Round Logic
    # - Display the current hangman
    # - Display the character set (and show correct and incorrect guesses)
    # - Ask user for input
    # - Check to see if game completes 

    
    # Users Guess
    while gameRunning:
        userGuess = input("Letter: ")


# Start of the game
def intro_msg():
    welcome_msg = """ 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

                        Welcome to Hangman!

            > You have 6 attempts to save hangman. 
            > Type a letter to submit your guess.

                          ... Good luck!
    
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    """

    print(welcome_msg)


# Hangman images in global array
hangmanPics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# Calling the game functions
intro_msg()
play_game()


# Testing - Ignore
#hello = input("Test test test")    
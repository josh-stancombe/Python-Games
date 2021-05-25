import random

# Global Variables
userPoints = 0
computerPoints = 0

def playRound(user_choice):
    global userPoints
    global computerPoints

    # Generate computer choice
    computer_choice_int = random.randint(1,3)

    if computer_choice_int == 1:
        computer_choice = "rock"
    elif computer_choice_int == 2:
        computer_choice = "paper"
    elif computer_choice_int == 3:
        computer_choice = "scissors"
    else:
        error("the computer choice")
    
    # Print Results
    print("\nThe computer threw:", computer_choice, "\n\n")
        
    # Decide Winner
    winner = ""
    result_msg = ""

    if user_choice == computer_choice:
        winner = "draw"

    elif user_choice == "rock":
        if computer_choice == "scissors":
            winner = "user"
        else:
            winner = "computer"
    
    elif user_choice == "paper":
        if computer_choice == "rock":
            winner = "user"
        else:
            winner = "computer"
    
    elif user_choice == "scissors":
        if computer_choice == "paper":
            winner = "user"
        else:
            winner = "computer"
    
    else:
        error("the winner")
    
    # Conclude Round
    if winner == "user":
        result_msg = "You won this round! :)"
        userPoints += 1
    elif winner == "computer":
        result_msg = "The computer won this round! :("
        computerPoints += 1
    elif winner == "draw":
        result_msg = "The round was a tie!"
    else:
        error("the results")

    print(result_msg, "\n")
    print("The current score is: You:", userPoints, "// Computer:", computerPoints,"\n")
    

def getUserChoice():    
    chosen = False
    choice = ""

    while chosen == False:
        rawUserChoice = input("Your move: ")
        userChoice = rawUserChoice.lower()
        
        if userChoice == "rock" or userChoice == "paper" or userChoice == "scissors":
            choice = userChoice    
            chosen = True
        else:
            print("\nSorry, I don't understand that. Please try again.\n")
    
    return choice


def playGame():
    round = 1
    while (userPoints < 3 and computerPoints < 3):      
        print("\n------- Round ", round , " -------\n")
        user_choice = getUserChoice()
        playRound(user_choice)
        round += 1
    summary()


def intro_msg():
    welcome_msg = """ 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

                        Welcome to Rock, Paper, Scissors!

            > You will play against the computer. 
            > The first player to win three rounds wins overall.
            > Type 'Rock', 'Paper' or 'Scissors' to play the round...

                                ... Good luck!
    
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    """
    print(welcome_msg)


def end_msg():
    finished_msg = "\nThanks for playing... See you next time! \n"
    print(finished_msg)
    input("Hit 'Enter' to Exit")
    exit()

def summary():
    if userPoints == 3:
        print("""
- - - - - - - - - - - - - - - - - - - - - - -
 __   __           __        ___       _ 
 \ \ / /__  _   _  \ \      / (_)_ __ | |
  \ V / _ \| | | |  \ \ /\ / /| | '_ \| |
   | | (_) | |_| |   \ V  V / | | | | |_|
   |_|\___/ \__,_|    \_/\_/  |_|_| |_(_)

- - - - - - - - - - - - - - - - - - - - - - -                                                                                          
        """)
    elif computerPoints == 3:
        print("""
 - - - - - - - - - - - - - - - - - - - - - - - - - - 

 __   __            _                         __ 
 \ \ / /__  _   _  | |    ___  ___  ___    _ / / 
  \ V / _ \| | | | | |   / _ \/ __|/ _ \  (_) |  
   | | (_) | |_| | | |__| (_) \__ \  __/   _| |  
   |_|\___/ \__,_| |_____\___/|___/\___|  (_) |  
                                             \_\ 

- - - - - - - - - - - - - - - - - - - - - - - - - - 
        """)
    else:
        error("the end of the game")


def error(area):
    print("Hmm, looks like I've got an error when i'm calculating", area, "! Sorry about that, how embarrassing!")
    exit()

intro_msg()
playGame()
end_msg()
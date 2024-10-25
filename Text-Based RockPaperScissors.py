#Rock_Paper_Scissors.py

#Name of Developer
print("This is EDET Eti-Abasi-Laurel’s First Project")
print("")

#Import the 'random' library to allow the game be played fairly
import random

#Define a function 'player_vs_computer()' for the game
def player_vs_computer():
    #Ask for user's name
    user_name = input ("Hmmm, yet another human who thinks he can best a machine. What's your name? ") 
    #Display a welcome message for the player
    print("Well,", user_name, ",welcome to Rock, Paper, Scissors! Let's have a fair game!")

    #Create an array 'options' which stores valid options for the game
    choices = ['rock', 'paper', 'scissors']
    
    #Starts a loop which will run the game until the player ends it
    while True:
        player_choice = ""
        
        #Obtain valid input from player until a correct choice is made
        while player_choice not in choices:
            #Ask player for their choice and convert it to lowercase for easier convention
            player_choice = input("\nPlease choose your weapon from the options [rock, paper, or scissors]: ").lower()
            #Keep asking for input if player enters something invalid
            if player_choice not in choices:
                print("Invalid input. Please enter either 'rock', 'paper', or 'scissors'.")

        #For sake of fairness, randomise the computer's choice and print
        computer_choice = random.choice(choices)
        print("'Computer' chose " + computer_choice)

        #Give possible outcomes of the match-up
        print ("")
        if player_choice == computer_choice:
            print("A tie?? Hahahaha! That was probably a fluke, won't happen next time though.")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            print("I lo-lo-lost? How??? I have to say, I did take you for granted, my apologies O' great warrior.")
        else:
            print("What did I say? Let's play again! I want to keep my perfect streak vs humans.")

        #Ask player if they would like to play again
        play_again = ""
        #Keep asking until player enters a valid input
        while play_again not in ["yes", "no"]:
            play_again = input("\nLet's battle again! What do you say? (yes/no): ").lower()
            if play_again not in ["yes", "no"]:
                print("Invalid input. Please enter either 'yes' or 'no'.")

        #If the player chooses 'no', exit loop and end game, otherwise continue loop
        if play_again != 'yes':
            break

    #Print a cheerful message
    print("I won't lie, I'm disheartened that you'd run away from our fight. However, fret not, I'll always remember the name", user_name, "as mankind's strongest.")

#Call the function to start the game
player_vs_computer()
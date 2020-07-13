# This game replicates "rock, paper, scissors" in the command line.
# In this game you can play against a computer opponent in two game modes:
# In Random mode the computer will select rock, paper, or scissors based on Python's Random module;
# In Tactical mode the computer selects based on real-world game theory research into this game.
# You should be asked for your mode choice at the start of the game, your choice for the game,
# and then whether you would like to play another round.


import random


# Random mode has the computer select at random
# Tactical mode has the computer select based on the player's last move.
def choose_game_mode():
    while True:
        mode_choice = input("Select game mode: random(1) or tactical(2) ")
        if mode_choice == "1" or mode_choice == "2":
            return mode_choice
        else:
            pass


def player_choice():
    while True:
        choice_input = input("Pick rock(r), paper(p), or scissors(s) ")
        if choice_input == "r" or choice_input == "p" or choice_input == "s":
            return choice_input
        else:
            pass


choice_dict = {
    1: "r",
    2: "p",
    3: "s"
}


result_dict = {
    "r": {
        "r": "draw",
        "p": "lose",
        "s": "win"
    },
    "p": {
        "r": "win",
        "p": "draw",
        "s": "lose"
    },
    "s": {
        "r": "lose",
        "p": "win",
        "s": "draw"
    }
}


# have computer select
def random_mode():
    player = player_choice()
    computer_choice = choice_dict.get(random.randint(1, 3))
    print(player)
    print(computer_choice)
    print(result_dict[player][computer_choice])


# These global variables are the results of the last round in tactical mode
# They need to be outside the tactical mode function as they are set in one iteration,
# and called in the next.
last_computer_choice = "a"
last_player_choice = "a"
won = None


# tactical mode applies the findings of game theory research into 'rock, paper, scissors' to our game
def tactical_mode():
    player = player_choice()
    global last_player_choice
    global last_computer_choice
    global won
    # if won means the computer lost.  Thus expect player to do the same again, so pick the third.
    if won == "win":
        choices = list(choice_dict.values())
        choices.remove(last_computer_choice)
        choices.remove(last_player_choice)
        computer = choices.pop()
    # won is false means computer won.  Play last player choice
    elif won == "lose":
        computer = last_player_choice
    # if the last game was drawn, computer should play what would have lost in the last round.
    elif won == "draw":
        if last_player_choice == "r":
            computer = "s"
        elif last_player_choice == "p":
            computer = "r"
        else:
            computer = "p"
    # this is if "won" hasn't been set: the starting condition for round 1
    else:
        computer = "s"

    last_player_choice = player
    last_computer_choice = computer

    print("last computer choice is", last_computer_choice)
    print("last player choice is", last_player_choice)
    print(result_dict[player][computer])

    won = result_dict[player][computer]


# function to ask if the user wants to play again
def play_again():
    while True:
        again = input("Play again? (y/n) ")
        if again == "y":
            return "y"
        elif again == "n":
            return "n"
        else:
            pass


# run game logic
def run_game():
    print("Welcome to Rock, Paper, Scissors")
    mode = choose_game_mode()
    keep_playing = True
    while keep_playing:
        if mode == "1":
            random_mode()
        else:
            tactical_mode()
        again = play_again()
        if again == "n":
            keep_playing = False
        else:
            pass


run_game()



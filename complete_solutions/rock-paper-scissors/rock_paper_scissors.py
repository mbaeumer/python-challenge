
import random
from game_result import GameResult

def show_options():
    choice = ""
    while choice != "R" and choice != "P" and choice != "S" and choice != "X":
        print("R - Rock")
        print("P - Paper")
        print("S - Scissors")
        print("X - End")
        choice = input("Your choice: ")
    return choice

def start_game():
    while 1==1:
        choice = show_options()
        if choice != "X":
            computer_choice = make_choice()
            result = check_result(computer_choice, choice)
            show_result(result)
        else:
            print("End")
            break

def check_result(computer_choice, player_choice):
    if computer_choice == player_choice:
        return GameResult.DRAW

    if computer_choice == "R" and player_choice == "P":
        return GameResult.COMPUTER_LOOSE
    elif computer_choice == "R" and player_choice == "S":
        return GameResult.COMPUTER_WIN
    elif computer_choice == "P" and player_choice == "R":
        return GameResult.COMPUTER_WIN
    elif computer_choice == "P" and player_choice == "S":
        return GameResult.COMPUTER_LOOSE
    elif computer_choice == "P" and player_choice == "R":
        return GameResult.COMPUTER_WIN

def show_result(result):
    if result == GameResult.COMPUTER_WIN:
        print("I win!")
    elif result == GameResult.COMPUTER_LOOSE:
        print("You win")
    else:
        print("Nobody wins")

def make_choice():
    my_choice = ""
    random_choice = random.randint(1,3)
    if random_choice == 1:
        my_choice = "R"
    elif random_choice == 2:
        my_choice = "P"
    else:
        my_choice = "S"
    return my_choice

if __name__ == "__main__":
    start_game()
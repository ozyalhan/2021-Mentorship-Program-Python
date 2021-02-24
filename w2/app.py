"""
This project aims to introduce my mentees basic of python with all fundamental methods.

Game Concept is Rock Paper Scissors and everyone plays this game even one time in life.

Rock smashes scissors.
Paper covers rock.
Scissors cut paper.

You play this game aganist computer and who will the 3 as score will be winner!
"""

import random


def main():
    """Runs Main Function"""  # docstring
    user_score = 0
    computer_score = 0

    # Game Mechanism on Terminal
    while True:
        user = get_user_choice()

        computer = get_computer_choice()

        user_score, computer_score = compare(
            user, computer, user_score, computer_score)

        score_control(user_score, computer_score)


def score_control(user_s, computer_s):
    """Gets user and computer scores as integer and if one of them reach 3, complete the game"""
    if user_s == 3 or computer_s == 3:
        if user_s == 3:
            print("You Win the Game!")
            exit()
        else:
            print("Computer Wins the Game!")
            exit()


def compare(user_val, computer_val, user_score, computer_score):
    """Get user_val and computer_val, and evalutes game rule. Gets user_score and computer score and return both in every case.
        - Rock smashes scissors.
        - Paper covers rock.
        - Scissors cut paper.
    """

    game_choice_dict = {0: "Rock", 1: "Paper", 2: "Scissors"}

    if user_val != computer_val:

        if (user_val == 1 and computer_val == 0) or (user_val == 2 and computer_val == 1) or (user_val == 0 and computer_val == 2):
            print("User Wins")
            user_score += 1

        elif (user_val == 0 and computer_val == 1) or (user_val == 1 and computer_val == 2) or (user_val == 2 and computer_val == 0):
            print("Computer Wins")
            computer_score += 1
    else:
        print("Draw! You choose the same!")

    print("User showed:{} | Computer shoved:{}".format(
        game_choice_dict.get(user_val), game_choice_dict.get(computer_val)))
    print("User Score:{} | Computer Score:{}\n-----".format(user_score, computer_score))
    return user_score, computer_score


def get_computer_choice():
    """Return value between 0 to 2 for computer choice of the game"""
    computer_choice = random.randint(0, 2)
    return computer_choice


def get_user_choice():
    """Get user input and return it as integer value"""

    # TODO In try-except block recursive structure should be control with local variable. It will be handle in recursive functions subject.
    try:
        user_choice = int(input("Rock[0], Paper[1], Scisscors[2]: ").strip())
        if user_choice not in [0, 1, 2]:
            print("Please write input only 0, 1, 2.")
            return get_user_choice()

        return user_choice

    except ValueError:
        print("Error: You wrote wrong input, Please write input only 0, 1, 2.")
        return get_user_choice()


if __name__ == "__main__":

    main()

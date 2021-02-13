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
    if user_s == 3 or computer_s == 3:
        if user_s == 3:
            print("Kazanan sensin")
            exit()
        else:
            print("PC kazandı.")
            exit()


def compare(user_val, computer_val, user_score, computer_score):
    if user_val != computer_val:
        if user_val == 1 and computer_val == 0:
            print("User Win")
            user_score += 1
            print("User Score:{} | Computer Score:{}".format(
                user_score, computer_score))
            return user_score, computer_score

        elif user_val == 0 and computer_val == 1:
            print("Computer Win")
            computer_score += 1
            print("User Score:{} | Computer Score:{}".format(
                user_score, computer_score))
            return user_score, computer_score

        elif user_val == 2 and computer_val == 1:
            print("User Win")
            user_score += 1
            print("User Score:{} | Computer Score:{}".format(
                user_score, computer_score))
            return user_score, computer_score

        elif user_val == 1 and computer_val == 2:
            print("Computer Win")
            computer_score += 1
            print("User Score:{} | Computer Score:{}".format(
                user_score, computer_score))
            return user_score, computer_score

        elif user_val == 0 and computer_val == 2:
            print("User Win")
            user_score += 1
            print("User Score:{} | Computer Score:{}".format(
                user_score, computer_score))
            return user_score, computer_score

        elif user_val == 2 and computer_val == 0:
            print("Computer Win")
            computer_score += 1
            print("User Score:{} | Computer Score:{}".format(
                user_score, computer_score))
            return user_score, computer_score

    else:
        print("You choose the same!")
        print("User Score:{} | Computer Score:{}".format(
            user_score, computer_score))
        return user_score, computer_score


def get_computer_choice():
    computer_choice = random.randint(0, 2)  # 0 1 ya da 2 döner
    return computer_choice


def get_user_choice():
    # burayı geliştir
    user_choice = int(input("Rock[0], Paper[1], Scisscors[2]: "))
    return user_choice


if __name__ == "__main__":

    main()

"""
            Abdullah Baig - 231485698
            Hamza Asaad   - 231450993

"""

###   Please run this file to start the game   ###

from bulls_and_cows import *


if __name__ == "__main__":
    play_again_flag = True

    # a loop which ends when user enters 'Q' or 'N'. start_game() function in bulls_and_cows.py returns false in that
    # case and the loop ends otherwise true is returned and a new game starts
    while play_again_flag:
        play_again_flag = start_game()

    # when user quits then exit msg is printed to terminal
    BullsAndCows.print_exit_msg()

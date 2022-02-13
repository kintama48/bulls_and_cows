"""
            Abdullah Baig - 231485698
            Hamza Asaad   - 231450993

"""

###   Please run this file to start the game   ###

from bulls_and_cows import *


if __name__ == "__main__":
    play_again_flag = True

    while play_again_flag:
        play_again_flag = start_game()

    BullsAndCows.print_exit_msg()

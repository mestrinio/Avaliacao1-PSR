#!/usr/bin/env python3


# Avaliação 1 PSR - Typing test
# 12/10/2023
# 1 - Beatriz Marques; 2 - Pedro Martins; 3 - Tiago Pereira
import argparse

# Import the necessary modules
import readchar
from functions import *
from colorama import Fore, Back, Style

def main():
    parser = argparse.ArgumentParser(description = 'Definition os test mode')
    parser.add_argument('-utm', '--use_time_mode', help='Max number of secs for time mode or maximum number of inputs for number of inputs mode', action='store_true')
    parser.add_argument('-mv MAX_VALUE', '--max_value Max_VALUE', help= 'Max number of second for time mode or maximum number of inputs for number of inputs mode', required=True)
    parser.add_argument('-uw', '--use_words', help='Use word typing mode, instead of a single character typing.', action='store_true')
   

    args = parser.parse_args()

    flag = True
    words_from_file = []
    read_file(words_from_file)
    print("Press '1' to the challenge with letter or '2' to the challenge with complet words:")    
    MODE = readchar.readkey()
    while MODE != '1' and MODE != '2':
        print("Press '1' to the challenge with letter or '2' to the challenge with complet words:")    
        MODE = readchar.readkey()

    print("Press any key to start the challenge")
    readchar.readkey()


    while flag == True:
        if MODE == '1':
            flag = generate_random_letter()
        else:
            flag = generate_random_words(words_from_file)



    print("End of the challenge")

if __name__ == '__main__':

    main()

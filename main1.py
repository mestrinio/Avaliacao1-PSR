#!/usr/bin/env python3


# Avaliação 1 PSR - Typing test
# 12/10/2023
# 1 - Beatriz Marques; 2 - Pedro Martins; 3 - Tiago Pereira


# Import the necessary modules
import argparse
import readchar
from functions1 import *
from colorama import Fore, Back, Style
from collections import namedtuple
import time

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
    test_start = time.time()
    number_of_types = 0
    number_of_hits = 0
    inputs = []

    while flag == True:
        if MODE == '1':
            flag,input = generate_random_letter()
            if input:
                if input.requested == input.received:
                    number_of_hits += 1
                number_of_types += 1
                inputs.append(input)
            
              


        else:
            flag = generate_random_words(words_from_file)

        print(args)
#        if number_of_types== args.2


    test_end = time.time()
    test_duration = test_start - test_end
    accuracy = number_of_hits/number_of_types
    type_average_duration = 0
    type_hit_average_duration = 0
    type_miss_average_duration = 0


    print("End of the challenge")

if __name__ == '__main__':

    main()

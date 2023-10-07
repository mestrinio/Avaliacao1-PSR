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
   
    args = vars(parser.parse_args()) # creates a dictionary
    
    flag = True
    words_from_file = []
    read_file(words_from_file)

    if args['use_words']:
        print("Press '1' to use real words or '2' to use words with random caracters:")
        mode_word_generator = readchar.readkey()
        while mode_word_generator != '1' and mode_word_generator != '2':
           print("Press '1' to use real words or '2' to use words with random caracters:")
           mode_word_generator = readchar.readkey()


    print("Press any key to start the challenge")
    readchar.readkey()


    while flag == True:
        if args['use_words']:
            flag = generate_random_words(words_from_file, mode_word_generator)
        else:
            flag = generate_random_letter()
            


    print("End of the challenge")

if __name__ == '__main__':

    main()

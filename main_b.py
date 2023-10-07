#!/usr/bin/env python3


# Avaliação 1 PSR - Typing test
# 12/10/2023
# 1 - Beatriz Marques; 2 - Pedro Martins; 3 - Tiago Pereira
import argparse
from my_functions import time_mode
from time import time, ctime

def main():

    parser = argparse.ArgumentParser(description = 'Definition os test mode')
    parser.add_argument('-utm', '--use_time_mode', help='Max number of secs for time mode or maximum number of inputs for number of inputs mode', action='store_true')
    parser.add_argument('-mv', '--max_value', type = int, help= 'Max number of second for time mode or maximum number of inputs for number of inputs mode',required=True)
    parser.add_argument('-uw', '--use_words', help='Use word typing mode, instead of a single character typing.', action='store_true')
   

    args = vars(parser.parse_args())

    #verifies id we are in the time mode
    if args['use_time_mode']:
        print('You selected the time mode. Your test will last ' + str(args['max_value']) + ' seconds')
        #verifies if the user selected the word typing mode
        if args['use_words']:
            print('Once you have chosen the word typing mode, random words will be generated that you will nedd to reproduce until the time runs out')
        
        print('To start the test, press any key, and to stop the test before it finishes, press the space key')
        print('Good luck')
        time_mode(args['max_value'])
        #print(''.join(inputs))
    




if __name__ == '__main__':
    main()
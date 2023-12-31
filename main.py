#!/usr/bin/env python3


# Avaliação 1 PSR - Typing test
# 12/10/2023
# 1 - Beatriz Marques; 2 - Pedro Martins; 3 - Tiago Pereira
import argparse, readchar
from my_functions import time_mode, inputs_mode, statistics
from time import time, ctime
from collections import namedtuple
from pprint import pprint

def main():

    parser = argparse.ArgumentParser(description = 'Definition os test mode')
    parser.add_argument('-utm', '--use_time_mode', help='Max number of secs for time mode or maximum number of inputs for number of inputs mode', action='store_true')
    parser.add_argument('-mv', '--max_value', type = int, help= 'Max number of second for time mode or maximum number of inputs for number of inputs mode',required=True)
    parser.add_argument('-uw', '--use_words', help='Use word typing mode, instead of a single character typing.', action='store_true')
   

    args = vars(parser.parse_args())

    inputs_list = []
 

    
    if args['use_time_mode']: #verifies id we are in the time mode
        print('\nYou selected the time mode. Your test will last ' + str(args['max_value']) + ' seconds')
        
        if args['use_words']: #verifies if the user selected the word typing mode
            
            print('\nOnce you have chosen the word typing mode, random words will be generated that you will nedd to reproduce until the time runs out')
            word_type = int(input('\nWould you like the words to be: \n1 - Randomly generated \n2 - Randomly chosen from a file with multiple example words?\n'))
            if (word_type == 1):
                maximum_size = int(input('\nWhat is the maximum size/length you would like for the generated words?\n'))
                while maximum_size <= 1 :
                    maximum_size = int(input('Maximum size must be higher than 1!\n'))
            else:
                maximum_size = 0
        else:
            
            print('\nOnce you have chosen the letter typing mode, random characters will be generated that you will need to reproduce until the time runs out')
            maximum_size = 1
        
        print('\nTo start the test, press any key, and to stop the test before it finishes, press the space key')
        print('Good luck')
        readchar.readkey()

        inputs_list, test_duration, test_start, test_end=time_mode(args['max_value'], maximum_size)
    
    else:
        print('\nYou selected the inputs mode. To complete the test, you need do insert ' + str(args['max_value']) + 'inputs')

        if args['use_words']: #verifies if the user selected the word typing mode
            
            print('\nOnce you have chosen the word typing mode, random words will be generated that you will need to reproduce until the time runs out')
            word_type = int(input('\nWould you like the words to be: \n1 - Randomly generated \n2 - Randomly chosen from a file with multiple example words?\n'))
            if (word_type == 1):
                maximum_size = int(input('\nWhat is the maximum size/length you would like for the generated words?\n'))
                while maximum_size <= 0 :
                    maximum_size = int(input('Maximum size must be a positive number!\n'))
            else:
                maximum_size = 0
        else:
            
            print('\nOnce you have chosen the letter typing mode, random characters will be generated that you will need to reproduce until the time runs out')
            maximum_size = 1
        
        print('\nTo start the test, press any key, and to stop the test before it finishes, press the space key')
        print('Good luck')
        readchar.readkey()

        inputs_list, test_duration, test_start, test_end = inputs_mode(args['max_value'], maximum_size)
    



    
    number_of_hits, number_of_types, type_average_duration, type_hit_average_duration, type_miss_average_duration = statistics(inputs_list)

    if(number_of_types == 0):
        accuracy = 0
    else:
        accuracy = round(number_of_hits/number_of_types,2)

    results = {
        'accuracy': accuracy,
        'inputs': inputs_list,
        'number_of_hits': number_of_hits,
        'number_of_types': number_of_types,
        'test_duration': test_duration,
        'test_end': ctime(test_end),
        'test_start': ctime(test_start),
        'type_average_duration': type_average_duration,
        'type_hit_average_duration': type_hit_average_duration,
        'type_miss_average_duration': type_miss_average_duration
    }

    pprint(results)




if __name__ == '__main__':
    main()

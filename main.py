#!/usr/bin/env python3


# Avaliação 1 PSR - Typing test
# 12/10/2023
# 1 - Beatriz Marques; 2 - Pedro Martins; 3 - Tiago Pereira
import argparse


def main():
    parser = argparse.ArgumentParser(description = 'Definition os test mode')
    parser.add_argument('-utm', '--use_time_mode', help='Max number of secs for time mode or maximum number of inputs for number of inputs mode', action='store_true')
    parser.add_argument('-mv MAX_VALUE', '--max_value Max_VALUE', help= 'Max number of second for time mode or maximum number of inputs for number of inputs mode', required=True)
    parser.add_argument('-uw', '--use_words', help='Use word typing mode, instead of a single character typing.', action='store_true')
   

    args = parser.parse_args()



if __name__ == '__main__':
    main()

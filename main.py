#!/usr/bin/env python3


# Avaliação 1 PSR - Typing test
# 12/10/2023
# 1 - Beatriz Marques; 2 - Pedro Martins; 3 - Tiago Pereira

# Import the necessary modules
import readchar
from functions import *
from colorama import Fore, Back, Style

def main():

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
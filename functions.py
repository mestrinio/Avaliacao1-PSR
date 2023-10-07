
# Use imports here
from colorama import Fore, Back, Style
import random, readchar

#  Create a list from the file words.txt and return it
def read_file(words):
    # Read the file
    file = open("words.txt", "r")
    for line in file:
        words.extend(line.split())
    file.close()

    return words


# Generate a random letter or word and ask the user to type it
def generate_random_letter():
    
    letter = chr(random.randint(97, 122))
    print("You should type the letter: ", letter)
    print("Type the letter: ")
    INPUT = readchar.readkey()
    if INPUT == ' ':
           return False
    elif INPUT == letter:
           #addDictionary(INPUT)
       print("You typed: " + Fore.GREEN + INPUT + Fore.RESET)
    else:
           #AddDictionary(INPUT)
        print("You typed: ", Fore.RED + INPUT + Fore.RESET)
    return True

def generate_random_words(words_from_file):
    word2write= random.choice(words)
    print("You should type the word: ", word2write)

    INPUT = input("Type the word: ")
    if INPUT == ' ':
        return False
    elif INPUT == word2write:
            #addDictionary(INPUT)
        print("You typed: " + Fore.GREEN + INPUT + Fore.RESET)
    else:
            #AddDictionary(INPUT)
        print("You typed: ", Fore.RED + INPUT + Fore.RESET)
    return True

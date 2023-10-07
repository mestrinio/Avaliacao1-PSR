from time import time, ctime
from colorama import Fore, Back, Style
import random, readchar

#function for time mode
def time_mode(max_time):
    initial_time = time()
    elapsed_time= 0
    exit = False
    inputs_list = []
    while(elapsed_time <= max_time and exit==False):
        exit, input_data =generate_random_letter()
        inputs_list.append(input_data)
        elapsed_time = time() - initial_time
    print('Duration of the test: ' + str(elapsed_time))
    print (inputs_list)



#function for maximum inputs mode


#function for word generator



# Generate a random letter or word and ask the user to type it
def generate_random_letter():
    
    letter = chr(random.randint(97, 122))
    print("You should type the letter: ", letter)

    print("Type the letter: ")
    request_time = time()
    INPUT = readchar.readkey()
    input_data = {
        'requested': letter,
        'received': INPUT,
        'duration': (time() - request_time)
    }
    if INPUT == ' ':
           print('You exited the test')
           return True, input_data
    elif INPUT == letter:
           #addDictionary(INPUT)
       print("You typed: " + Fore.GREEN + INPUT + Fore.RESET)
    else:
           #AddDictionary(INPUT)
        print("You typed: ", Fore.RED + INPUT + Fore.RESET)
    return False, input_data
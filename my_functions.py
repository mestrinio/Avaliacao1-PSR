from time import time, ctime
from colorama import Fore, Back, Style
import random, readchar, string
from collections import namedtuple

#function for time mode
def time_mode(max_time, word_size):
    initial_time = time()
    elapsed_time= 0
    exit = False
    inputs_list = []
    while(elapsed_time <= max_time and exit==False):
        if word_size == 1:
            exit, input_data =generate_random_letter()
        else:
            exit, input_data =generate_random_word(word_size)
        if exit == False:
            inputs_list.append(input_data)
        
        elapsed_time = time() - initial_time
    
    print('Duration of the test: ' + str(elapsed_time))
    end_time = initial_time + elapsed_time
    return inputs_list,elapsed_time,initial_time, end_time



#function for maximum inputs mode


#function for word generator
def generate_random_word(maximum_size):

    size = random.randint(2,maximum_size) #word size
    letters = string.ascii_lowercase #we only use lowercase letters
    random_word = ''.join(random.choice(letters) for _ in range(size))

    Input = namedtuple('Input',['requested','received','duration'])
    print("You should type the word: ", random_word)

    print("Type the word: ")
    INPUT = ''
    request_time = time()
    for letter in random_word:
        char = readchar.readkey()
        INPUT += char
    
    input_data = Input(requested=random_word, received=INPUT, duration=(time()-request_time))
    if INPUT == ' ':
           print('You exited the test')
           return True, input_data
    elif INPUT == random_word:
       print("You typed: " + Fore.GREEN + INPUT + Fore.RESET)
    else:
        print("You typed: ", Fore.RED + INPUT + Fore.RESET)
    return False, input_data





# Generate a random letter or word and ask the user to type it
def generate_random_letter():

    Input = namedtuple('Input',['requested','received','duration'])
    letter = chr(random.randint(97, 122))
    print("You should type the letter: ", letter)

    print("Type the letter: ")
    request_time = time()
    INPUT = readchar.readkey()
    input_data = Input(requested=letter, received=INPUT, duration=(time()-request_time))
    if INPUT == ' ':
           print('You exited the test')
           return True, input_data
    elif INPUT == letter:
       print("You typed: " + Fore.GREEN + INPUT + Fore.RESET)
    else:
        print("You typed: ", Fore.RED + INPUT + Fore.RESET)
    return False, input_data




#calculates the statistics of the user
def statistics(inputs_list):

    number_of_types = len(inputs_list)
    number_of_hits = 0
    type_hit_average_duration = 0
    type_miss_average_duration = 0
    type_average_duration = 0

    for input_data in inputs_list:
        if(input_data.requested == input_data.received):
            number_of_hits+=1
            type_hit_average_duration+= input_data.duration
        else:
            type_miss_average_duration+= input_data.duration
        
        type_average_duration+= input_data.duration
    
    if(number_of_types == 0):
        type_average_duration = 0
    else:
        type_average_duration = type_average_duration/number_of_types

    if(number_of_hits == 0):
        type_hit_average_duration = 0
    else:
        type_hit_average_duration = type_hit_average_duration/number_of_hits

    if((number_of_types - number_of_hits) == 0):
        type_miss_average_duration = 0
    else:
        type_miss_average_duration = type_miss_average_duration/(number_of_types - number_of_hits)

    return number_of_hits, number_of_types, type_average_duration, type_hit_average_duration, type_miss_average_duration



from time import time, ctime
import signal
from colorama import Fore, Back, Style
import random, readchar, string
from collections import namedtuple

#Exception for timeout in time mode
class TimeoutExpired(Exception): 
    pass

def alarm_handler(signum, frame):
    raise TimeoutExpired

        
#function for time mode
def time_mode(max_time, word_size):

    initial_time = time()
    elapsed_time= 0
    exit = False
    inputs_list = []
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(max_time) # produce SIGALRM in `timeout` seconds
     

    try:
        while(exit==False):
            if word_size == 1:
                exit, input_data = generate_random_letter()
            elif word_size == 0:
                words = []
                read_file(words)
                exit, input_data = generate_random_words_from_file(words)
            else:
                exit, input_data = generate_random_word(word_size)
            
            if exit == False:
                inputs_list.append(input_data)
            
            elapsed_time = time() - initial_time
    except TimeoutExpired as e:
        elapsed_time = max_time
    
    print('\nDuration of the test: ' + str(elapsed_time))
    end_time = initial_time + elapsed_time
    return inputs_list,elapsed_time,initial_time, end_time



#function for maximum inputs mode
def inputs_mode(max_inputs,word_size):
    initial_time = time()
    exit = False
    inputs_list = []
    num_inputs = 0 #number of entered inputs

    while( num_inputs < max_inputs and exit == False):

        if word_size == 1:
            exit, input_data = generate_random_letter()
        elif word_size == 0:
            words = []
            read_file(words)
            exit, input_data = generate_random_words_from_file(words)
        else:
            exit, input_data = generate_random_word(word_size)
        
        if exit == False:
            inputs_list.append(input_data)
        
        num_inputs+= 1
    
    end_time = time()
    elapsed_time = end_time - initial_time
    print('\nDuration of the test: ' + str(elapsed_time))
    return inputs_list,elapsed_time,initial_time, end_time



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

#function for word generator
def generate_random_word(maximum_size):

    size = random.randint(2,maximum_size) #word size
    letters = string.ascii_lowercase #we only use lowercase letters
    random_word = ''.join(random.choice(letters) for _ in range(size))

    Input = namedtuple('Input',['requested','received','duration'])
    print("You should type the word: ", random_word)

    print("Type the word: ")
    request_time = time()
    INPUT = readchar.readkey()
    
    if INPUT == ' ':
           print('You exited the test')
           input_data = Input(requested=random_word, received=INPUT, duration=(time()-request_time))
           return True, input_data
    
    for i in range(1,len(random_word)):
        char = readchar.readkey()
        INPUT += char

    input_data = Input(requested=random_word, received=INPUT, duration=(time()-request_time))

    if INPUT == random_word:
       print("You typed: " + Fore.GREEN + INPUT + Fore.RESET)
    else:
        print("You typed: ", Fore.RED + INPUT + Fore.RESET)
    return False, input_data

#  Create a list from the file words.txt and return it
def read_file(words):
    # Read the file
    file = open("words.txt", "r")
    for line in file:
        words.extend(line.split())
    file.close()
    

def generate_random_words_from_file(words_from_file,):

    
    word2write= random.choice(words_from_file)

    Input = namedtuple('Input',['requested','received','duration'])
    print("You should type the word: ", word2write)

    print("Type the word: ")
    request_time = time()
    INPUT = readchar.readkey()

    if INPUT == ' ':
           print('You exited the test')
           input_data = Input(requested=word2write, received=INPUT, duration=(time()-request_time))
           return True, input_data
    
    for i in range(1,len(word2write)):
        char = readchar.readkey()
        INPUT += char
    
    input_data = Input(requested=word2write, received=INPUT, duration=(time()-request_time))

    if INPUT == word2write:
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
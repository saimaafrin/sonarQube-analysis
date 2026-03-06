
import string

def task_func(word):
    # Create a dictionary to map letters to their positions in the alphabet
    alphabet_position = {letter: (index + 1) for index, letter in enumerate(string.ascii_lowercase)}
    
    # Convert the word into a list of tuples
    result_list = [(letter.lower(), alphabet_position[letter.lower()]) for letter in word]
    
    return result_list
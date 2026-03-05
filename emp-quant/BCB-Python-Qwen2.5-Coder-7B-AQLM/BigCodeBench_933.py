
import string
import wordninja

def task_func(word):
    alphabet = string.ascii_lowercase
    letter_positions = {letter: index + 1 for index, letter in enumerate(alphabet)}
    tuple_list = [(letter, letter_positions[letter]) for letter in word.lower() if letter in letter_positions]
    
    # Split the word into a list of words using wordninja
    word_list = wordninja.split(word)
    
    return tuple_list, word_list
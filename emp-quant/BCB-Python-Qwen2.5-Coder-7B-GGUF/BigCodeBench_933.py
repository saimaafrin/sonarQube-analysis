
import string
import wordninja

def task_func(word):
    # Create a dictionary mapping each letter to its position in the alphabet
    alphabet_position = {letter: index for index, letter in enumerate(string.ascii_lowercase, start=1)}
    
    # Convert the word into a list of tuples with each tuple containing a letter and its position in the alphabet
    letter_positions = [(letter, alphabet_position[letter]) for letter in word.lower() if letter in alphabet_position]
    
    # Split the given word into a list of words using wordninja
    words_list = wordninja.split(word)
    
    return letter_positions, words_list
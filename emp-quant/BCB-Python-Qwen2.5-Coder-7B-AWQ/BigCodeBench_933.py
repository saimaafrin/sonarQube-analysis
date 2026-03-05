import string
import wordninja
def task_func(word):
    # Create a dictionary mapping each letter to its position in the alphabet
    alphabet_position = {letter: idx for idx, letter in enumerate(string.ascii_lowercase, start=1)}
    
    # Convert the word into a list of tuples
    word_tuples = [(letter, alphabet_position[letter]) for letter in word.lower()]
    
    # Split the given word into a list of words using wordninja
    split_words = wordninja.split(word)
    
    return word_tuples, split_words
word = "hello"
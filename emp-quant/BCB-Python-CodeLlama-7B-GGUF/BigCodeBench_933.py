
import string
import wordninja

def task_func(word):
    # Convert the word to a list of tuples
    word_list = list(zip(word, string.ascii_lowercase))

    # Split the word into a list of words
    words = wordninja.split(word)

    return words, word_list
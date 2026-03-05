import string
import wordninja
def task_func(word):
    """
    Converts a word into a list of tuples, with each tuple containing a lowercase English letter from the word and its position in the alphabet. Then, split the given word into a list of words.
    """
    # Convert the word into a list of tuples
    word_list = [(letter, string.ascii_lowercase.index(letter)) for letter in word]

    # Split the word into a list of words
    words = wordninja.split(word)

    return word_list, words
word = "hello"
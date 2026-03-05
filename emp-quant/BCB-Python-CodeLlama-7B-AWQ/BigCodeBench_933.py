import string
import wordninja
def task_func(word):
    """
    Converts a word into a list of tuples, with each tuple containing a lowercase English letter from the word and its position in the alphabet. Then, split the given word into a list of words.
    """
    # Create a list of tuples with each tuple consisting of a letter from the input string and its corresponding position in the alphabet.
    word_list = []
    for letter in word:
        if letter.isalpha():
            word_list.append((letter.lower(), string.ascii_lowercase.index(letter)))

    # Split the given word into a list of words.
    words = wordninja.split(word)

    return word_list, words
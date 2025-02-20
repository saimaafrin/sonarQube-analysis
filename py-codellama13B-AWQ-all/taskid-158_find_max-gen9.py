from typing import List

def find_max(words: List[str]) -> str:
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    >>> find_max(['name', 'of', 'string'])
    'string'
    >>> find_max(['name', 'enam', 'game'])
    'enam'
    >>> find_max(['aaaaaaa', 'bb', 'cc'])
    'aaaaaaa'
    """

    # initialize a dictionary to store each unique character and its count
    char_count = {}
    # initialize a variable to store the word with maximum unique characters
    max_word = ""
    # initialize a variable to store the maximum count
    max_count = 0

    # iterate over the input list
    for word in words:
        # reset the dictionary for each word
        char_count = {}
        # iterate over each character of the word
        for char in word:
            # check if the character is already present in the dictionary
            if char not in char_count:
                # if not present, add it to the dictionary with count 1
                char_count[char] = 1
            else:
                # if present, increment its count
                char_count[char] += 1
        # if the count of unique characters in this word is greater than
        # the maximum count seen so far, update the maximum count and the
        # word with maximum unique characters
        if len(char_count) > max_count:
            max_count = len(char_count)
            max_word = word

    # return the word with maximum unique characters
    return max_word

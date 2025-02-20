from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    >>> histogram('a b c')
    { 'a': 1, 'b': 1, 'c': 1 }
    >>> histogram('a b b a')
    { 'a': 2, 'b': 2 }
    >>> histogram('a b c a b')
    { 'a': 2, 'b': 2 }
    >>> histogram('b b b b a')
    { 'b': 4 }
    >>> histogram('')
    {  }

    """

    # create a dictionary to store the counts
    letter_counts = {}

    # iterate over each character in the string
    for character in test:
        # if the character is already in the dictionary
        if character in letter_counts:
            # increment the count
            letter_counts[character] += 1
        else:
            # otherwise set the count to 1
            letter_counts[character] = 1

    # create a variable to store the highest count
    highest_count = 0

    # iterate over each key in the dictionary
    for key in letter_counts:
        # if the count for this key is higher than the current highest count
        if letter_counts[key] > highest_count:
            # update the highest count
            highest_count = letter_counts[key]

    # create a dictionary to store the results
    result = {}

    # iterate over each key in the dictionary
    for key in letter_counts:
        # if the count for this key is equal to the highest count
        if letter_counts[key] == highest_count:
            # add the key and its count to the results
            result[key] = letter_counts[key]

    # return the results
    return result

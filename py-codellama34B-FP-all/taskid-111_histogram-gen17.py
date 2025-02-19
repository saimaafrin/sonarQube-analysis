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

    # Initialize a dictionary to store the letter and occurrence
    d: Dict[str, int] = {}
    max_occurrence = 0

    # Iterate over the string
    for letter in test:
        # If the letter is already in the dictionary, add 1 to its occurrence
        if letter in d:
            d[letter] += 1
        # If the letter is not in the dictionary, set its occurrence to 1
        else:
            d[letter] = 1

        # Check if the letter occurrence is the highest
        if d[letter] > max_occurrence:
            max_occurrence = d[letter]
    
    # Return the dictionary with only the letter that have the highest occurrence
    return {k:v for k,v in d.items() if v == max_occurrence}

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

    # Create an empty dictionary to store letter counts
    counts: Dict[str, int] = {}

    # Split the string into letters
    letters: list[str] = test.split()

    # Loop over the letters and update the dictionary counts
    for letter in letters:
        # Check if the letter exists in the dictionary
        if letter not in counts:
            # Set the initial count to 1
            counts[letter] = 1
        else:
            # Increment the count of the letter
            counts[letter] += 1

    return counts

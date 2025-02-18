from typing import List

def select_words(s: str, n: int) -> List[str]:
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    >>> select_words('Mary had a little lamb', 4)
    ['little']
    >>> select_words('Mary had a little lamb', 3)
    ['Mary', 'lamb']
    >>> select_words('simple white space', 2)
    []
    >>> select_words('Hello world', 4)
    ['world']
    >>> select_words('Uncle sam', 3)
    ['Uncle']
    """


    # Split the string into words
    words = s.split()

    # Initialize an empty list to store words that meet the condition
    result = []

    # Iterate over the words
    for word in words:
        # Initialize a counter for the number of consonants
        counter = 0

        # Iterate over the letters in the word
        for letter in word:
            # Check if the letter is a consonant
            if letter.lower() not in 'aeiou':
                # Increment the counter
                counter += 1
        
        # Check if the number of consonants is equal to n
        if counter == n:
            # Add the word to the list of words that meet the condition
            result.append(word)
    
    # Return the list of words
    return result

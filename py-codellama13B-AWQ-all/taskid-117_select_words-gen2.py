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

    # Initialize a counter to keep track of consonants
    consonant_count = 0
    # Initialize a list of words with n consonants
    word_list = []
    # Initialize a temporary word string
    temp_word = ''
    # Iterate through each character in s
    for char in s:
        # If the character is a letter
        if char.isalpha():
            # If the character is a consonant
            if char.lower() in 'bcdfghjklmnpqrstvwxyz':
                # Increment the consonant counter
                consonant_count += 1
            # If the consonant counter is equal to n
            if consonant_count == n:
                # If the character is a space
                if char.isspace():
                    # Add the temporary word to the word list
                    word_list.append(temp_word)
                    # Reset the temporary word
                    temp_word = ''
                    # Reset the consonant counter
                    consonant_count = 0
                # If the character is a letter
                else:
                    # Add the character to the temporary word
                    temp_word += char
            # If the consonant counter is greater than n
            elif consonant_count > n:
                # If the character is a space
                if char.isspace():
                    # Reset the consonant counter
                    consonant_count = 0
            else:
                # Add the character to the temporary word
                temp_word += char
    # Return the word list
    return word_list

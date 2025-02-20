def get_closest_vowel(word: str) -> str:
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    >>> get_closest_vowel('yogurt')
    'u'
    >>> get_closest_vowel('FULL')
    'U'
    >>> get_closest_vowel('quick')
    ''
    >>> get_closest_vowel('ab')
    ''
    """


    # Finds the index of the first vowel from the right.
    right_vowel_idx = -1
    for i in range(len(word)-1, -1, -1):
        if word[i].isalpha() and word[i].islower():
            right_vowel_idx = i
            break
    
    # Finds the index of the first vowel from the left.
    left_vowel_idx = -1
    for i in range(len(word)):
        if word[i].isalpha() and word[i].islower():
            left_vowel_idx = i
            break

    # If there is no vowel in the word, return the empty string.
    if right_vowel_idx == -1 and left_vowel_idx == -1:
        return ''

    # If the word is only one vowel, return the vowel.
    if right_vowel_idx == -1:
        return word[left_vowel_idx]
    elif left_vowel_idx == -1:
        return word[right_vowel_idx]

    # Check if the right and left vowels are consecutive.
    if abs(right_vowel_idx - left_vowel_idx) <= 1:
        return word[right_vowel_idx]
    else:
        return ''

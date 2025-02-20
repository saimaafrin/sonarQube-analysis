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

    # Get the position of the first vowel.
    first_vowel = word.find('a')
    # If the word does not contain a vowel, return ''
    if first_vowel == -1:
        return ''
    # Start with the first vowel, and try each position from the right-hand side
    for i in range(first_vowel, len(word)):
        # If the current character is a consonant,
        # and the next character is a vowel
        if word[i].isalpha() and word[i].islower() and word[i+1].isalpha() and word[i+1].isupper():
            return word[i+1]
        # If the current character is a vowel,
        # and the previous character is a consonant
        if word[i].isalpha() and word[i].isupper() and word[i-1].isalpha() and word[i-1].islower():
            return word[i]
    # If we get to the end and didn't find a vowel, return ''
    return ''

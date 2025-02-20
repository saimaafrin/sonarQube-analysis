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

    # Check if word is empty string
    if not word:
        return ''
    
    # Find all vowels in the word
    vowels = [char for char in word if char in 'AEIOUaeiou']

    # Check if the word doesn't contain any vowels
    if not vowels:
        return ''

    # Find the closest vowel
    for i, char in enumerate(word[::-1]):
        if char in 'AEIOUaeiou':
            return vowels[i]

    return ''

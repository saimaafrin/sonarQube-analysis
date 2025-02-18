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

    if len(word) < 2:
        return ''

    i = len(word) - 1

    while i > 0 and word[i - 1].isalpha():
        i -= 1

    if i == 0:
        return ''

    while i < len(word) - 1 and not word[i + 1].isalpha():
        i += 1

    return word[i]

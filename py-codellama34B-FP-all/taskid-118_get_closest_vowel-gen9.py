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

    word = word.upper()
    vowels = 'AEIOU'
    right = len(word) - 1
    left = right - 1
    while right >= 0 and left >= 0:
        if word[right] in vowels and word[left] not in vowels:
            return word[right]
        left -= 1
        right -= 1
    return ''

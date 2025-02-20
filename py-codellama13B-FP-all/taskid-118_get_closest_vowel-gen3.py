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

    vowels = ['a', 'e', 'i', 'o', 'u']
    last_consonant_index = -1
    found_vowel = False
    for i, c in enumerate(word[::-1]):
        if c.lower() in vowels:
            found_vowel = True
            break
        if c.isalpha() and c.lower() not in vowels:
            last_consonant_index = len(word) - 1 - i
    
    if found_vowel:
        return word[last_consonant_index + 1]
    else:
        return ''

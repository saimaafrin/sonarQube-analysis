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

    if len(word) < 3:
        return ''
    word = word[::-1]
    for index, char in enumerate(word):
        if index == 0 or index == len(word) - 1:
            continue
        if char.isalpha() and char.islower():
            if word[index - 1].isupper() and word[index + 1].isupper():
                return char
    return ''

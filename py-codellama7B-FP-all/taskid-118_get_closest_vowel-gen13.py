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

    # Your code here
    if len(word) == 1:
        return ''
    if len(word) == 2:
        if word[1] == word[0]:
            return ''
        return word[1]
    
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    for i in range(len(word) - 2, -1, -1):
        if word[i + 1] not in consonants:
            continue
        if word[i] in 'aeiouAEIOU':
            return word[i + 1]
    return ''

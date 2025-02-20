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
    word_len = len(word)
    if word_len == 0:
        return ''
    for i in range(word_len - 1, -1, -1):
        if word[i] in vowels and i + 1 < word_len:
            if word[i + 1] not in vowels:
                return word[i]
    return ''

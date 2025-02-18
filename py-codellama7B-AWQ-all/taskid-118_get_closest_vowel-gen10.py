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

    vowels = ['A', 'E', 'I', 'O', 'U']
    if word[0] in vowels:
        return ''
    for index in range(len(word)-1, -1, -1):
        if word[index] in vowels:
            if index == 0:
                return ''
            if word[index-1] not in vowels:
                return word[index]
            if word[index+1] not in vowels:
                return word[index]
            return ''
    return ''

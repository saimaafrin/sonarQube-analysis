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
    if len(word) <= 2:
        return ''

    for i in range(len(word)-2):
        if word[i].isalpha() and word[i+1].isalpha() and word[i+2].isalpha():
            if word[i].islower():
                return word[i+1]
            elif word[i+1].islower():
                return word[i]
            elif word[i+2].islower():
                return word[i+1]

    return ''

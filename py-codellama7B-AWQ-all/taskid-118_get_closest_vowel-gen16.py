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

    if word.lower() == word:
        word = word.upper()

    vowels = ['A', 'E', 'I', 'O', 'U']
    closest_vowel = ''
    for i in range(1, len(word)):
        if word[i] in vowels and word[i - 1].isupper() != word[i].isupper():
            closest_vowel = word[i]
            break
    return closest_vowel

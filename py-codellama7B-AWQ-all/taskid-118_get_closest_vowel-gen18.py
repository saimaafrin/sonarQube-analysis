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

    if not word:
        return ''

    def is_vowel(c):
        return c.isalpha() and c.islower() and c in 'aeiou'

    def is_consonant(c):
        return c.isalpha() and c.islower() and c not in 'aeiou'

    result = ''
    word = word[::-1]
    i = 0
    while i < len(word):
        if is_vowel(word[i]):
            result = word[i]
            break
        if not is_consonant(word[i]):
            i += 1
            continue
        if i + 1 < len(word) and is_vowel(word[i + 1]):
            result = word[i + 1]
            break
        i += 1
    return result[::-1]

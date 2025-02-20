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

    if len(word) <= 1:
        return ''

    vowels = 'aeiou'
    vowel_index = -1
    consonants = 'bcdfghjklmnpqrstvwxyz'
    consonant_index = -1
    for index, ch in enumerate(word):
        if ch in vowels:
            vowel_index = index
        if ch in consonants:
            consonant_index = index

    if vowel_index < 0 or consonant_index < 0:
        return ''

    left_side = word[0:vowel_index]
    right_side = word[vowel_index + 1:]
    if left_side == '' or right_side == '':
        return ''

    for ch in right_side:
        if ch in vowels:
            return ch

    return ''

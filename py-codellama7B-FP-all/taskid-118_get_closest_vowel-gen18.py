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

    if len(word) == 0:
        return ''

    consonants = ''
    for letter in word:
        if letter in 'qwertyuiopasdfghjklzxcvbnm':
            consonants += letter

    # if it is the last letter and it is a consonant
    if word[-1] in consonants:
        if len(word) > 1 and word[-2] in 'aeiou':
            return word[-1]
        else:
            return ''

    # if it is the first letter and it is a consonant
    if word[0] in consonants:
        if word[1] in 'aeiou':
            return word[0]
        else:
            return ''

    # if it is a consonant
    for i in range(1, len(word) - 1):
        if word[i] in consonants and word[i + 1] in 'aeiou':
            return word[i]

    return ''

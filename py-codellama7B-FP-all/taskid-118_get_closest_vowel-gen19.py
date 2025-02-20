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

    def is_vowel(c):
        return c in 'AaEeIiOoUu'

    vowels = [c for c in word if is_vowel(c)]
    if not vowels:
        return ''

    left_i = -1
    right_i = len(word)
    for i in range(right_i):
        c = word[i]
        if c.isalpha() and is_vowel(c):
            left_i = i
            break

    for i in range(left_i + 1, right_i):
        c = word[i]
        if c.isalpha() and is_vowel(c):
            right_i = i
            break

    if left_i == -1 or right_i == len(word):
        return ''

    return word[left_i + 1:right_i]

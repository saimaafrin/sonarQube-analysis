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

    # Write your code here
    word = word.upper()
    length = len(word)
    if length == 1 or length == 2:
        return ''
    for i in range(length-2, 0, -1):
        if word[i] in 'AEIOU':
            if word[i-1] not in 'AEIOU' and word[i+1] not in 'AEIOU':
                return word[i]
    return ''

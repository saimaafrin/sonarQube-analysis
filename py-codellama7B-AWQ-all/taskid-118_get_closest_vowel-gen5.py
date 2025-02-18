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

    left_index = -1
    right_index = -1

    for i, letter in enumerate(word):
        if letter in 'AEIOU':
            if left_index == -1:
                left_index = i
            right_index = i
            break

    if left_index == -1 or right_index == -1:
        return ''
    else:
        return word[left_index:right_index+1]

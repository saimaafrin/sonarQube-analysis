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

    left = 0
    right = len(word) - 1

    while left < right:
        if word[left].isalpha() and word[left].islower():
            if word[right].isalpha() and word[right].islower():
                if word[right].lower() != word[left].lower():
                    return word[right].upper()
                else:
                    right -= 1
            else:
                left += 1
        else:
            left += 1

    return ''

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

    # 1. find the last consonant
    # 2. find the next vowel, if not found, return ''
    # 3. return the vowel
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    last_consonant_idx = -1
    for i in range(len(word) - 1, -1, -1):
        if word[i].lower() not in vowels:
            last_consonant_idx = i
            break

    if last_consonant_idx == -1:
        return ''

    next_vowel_idx = -1
    for i in range(last_consonant_idx + 1, len(word)):
        if word[i].lower() in vowels:
            next_vowel_idx = i
            break

    if next_vowel_idx == -1:
        return ''

    return word[next_vowel_idx]

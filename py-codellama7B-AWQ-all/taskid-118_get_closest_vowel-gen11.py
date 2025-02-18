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

    # Step 1: Find the last consonant in the word
    vowel = ''
    for i in range(len(word)-1, -1, -1):
        if word[i] in 'aeiou':
            vowel = word[i]
            break
    if vowel == '':
        return ''

    # Step 2: Find the closest vowel after the last consonant
    for i in range(len(word)-1, -1, -1):
        if word[i] in 'aeiou' and word[i] != vowel:
            return word[i]

    return ''

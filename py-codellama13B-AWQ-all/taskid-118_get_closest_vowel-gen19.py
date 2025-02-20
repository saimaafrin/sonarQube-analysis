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


    word = word.upper()
    vowels = 'AEIOU'
    # find the last consonant
    last_consonant = ''
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            return ''
        if word[i].isalpha():
            last_consonant = word[i]
            break

    # find the first consonant before the last consonant
    first_consonant = ''
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            return ''
        if word[i].isalpha() and word[i] == last_consonant:
            first_consonant = word[i-1]
            break

    # find the closest vowel between them
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            if word[i] != 'A' and word[i] != 'E':
                return word[i]
            elif word[i] == 'A' and word[i+1] == 'E':
                return 'U'
            else:
                return 'E'

    return ''

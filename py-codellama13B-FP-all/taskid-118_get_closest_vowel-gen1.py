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

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    word = word.lower()
    consonant_counter = 0
    for i in range(len(word) - 1, -1, -1):
        if word[i] in vowels:
            consonant_counter = 0
            if word[i] != 'a' and word[i] != 'e':
                return word[i]
        else:
            consonant_counter += 1
        if consonant_counter == 2:
            break
    return ''

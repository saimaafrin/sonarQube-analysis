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


    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_indices = [i for i, x in enumerate(word) if x.lower() in vowels]

    for i in range(len(vowel_indices) - 1):
        index_left = vowel_indices[i]
        index_right = vowel_indices[i+1]

        if index_left >= 1 and index_right <= len(word) - 2:
            if index_right - index_left > 2:
                if word[index_left - 1].islower() and word[index_right + 1].islower():
                    return word[index_left]
                return ''

    return ''

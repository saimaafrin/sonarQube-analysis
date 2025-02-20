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

    vowels = ["a", "e", "i", "o", "u"]
    word_list = list(word)
    for i in range(len(word_list) - 1, -1, -1):
        if word_list[i] in vowels:
            if (word_list[i - 1].isalpha() and word_list[i + 1].isalpha()) or word_list[i] in vowels:
                return word_list[i]
    return ""

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

    word_list = list(word)
    # Find the position of first consonant
    first_consonant_pos = 0
    while first_consonant_pos < len(word_list) and word_list[first_consonant_pos].isalpha() and not word_list[first_consonant_pos].isupper():
        first_consonant_pos += 1

    if first_consonant_pos >= len(word_list):
        return ""

    # Find the position of last consonant
    last_consonant_pos = len(word_list) - 1
    while last_consonant_pos > first_consonant_pos and word_list[last_consonant_pos].isalpha() and not word_list[last_consonant_pos].isupper():
        last_consonant_pos -= 1

    if first_consonant_pos == last_consonant_pos:
        return ""

    # Check the middle part
    if word_list[first_consonant_pos].lower() in "aeiou":
        return word_list[first_consonant_pos]

    if word_list[last_consonant_pos].lower() in "aeiou":
        return word_list[last_consonant_pos]

    for i in range(first_consonant_pos + 1, last_consonant_pos):
        if word_list[i].lower() in "aeiou":
            return word_list[i]

    return ""

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


    # Replace all non-consonant letters with '.'
    word = word.replace("a", ".").replace("e", ".").replace("i", ".").replace("o", ".").replace("u", ".")
    # Split word into a list of characters
    word = list(word)
    # Find the last consonant letter on the right side
    last_consonant = -1
    for i in range(len(word) - 1, -1, -1):
        if word[i] != ".":
            last_consonant = i
            break
    if last_consonant == -1:
        return ""
    # Find the first consonant letter on the right side
    first_consonant = -1
    for i in range(last_consonant - 1, -1, -1):
        if word[i] != ".":
            first_consonant = i
            break
    if first_consonant == -1:
        return ""
    # Find the closest vowel between two consonant letters
    min_dist = float("inf")
    closest_vowel = ""
    for i in range(first_consonant, last_consonant + 1):
        if word[i] == ".":
            continue
        if abs(i - last_consonant) < min_dist:
            min_dist = abs(i - last_consonant)
            closest_vowel = word[i]
    return closest_vowel

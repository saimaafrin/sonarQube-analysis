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
    word = word.replace(" ", "")
    vowels = ["A", "E", "I", "O", "U"]
    consonants = [
        "B",
        "C",
        "D",
        "F",
        "G",
        "H",
        "J",
        "K",
        "L",
        "M",
        "N",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    left_index = len(word) - 1
    right_index = 0
    closest_vowel = ""

    for i in range(len(word)):
        if word[i] in vowels:
            left_index = i
            break
    for j in range(len(word) - 1, -1, -1):
        if word[j] in consonants:
            right_index = j
            break
    if left_index != right_index:
        for k in range(left_index + 1, right_index):
            if word[k] in vowels:
                closest_vowel = word[k]
                break
    return closest_vowel

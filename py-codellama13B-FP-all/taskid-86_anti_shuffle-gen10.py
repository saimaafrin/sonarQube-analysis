def anti_shuffle(s: str) -> str:
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    >>> anti_shuffle('Hi')
    'Hi'
    >>> anti_shuffle('hello')
    'ehllo'
    >>> anti_shuffle('Hello World!!!')
    'Hello !!!Wdlor'
    """

    # find all words in the string
    words = s.split()
    # sort each word in alphabetical order
    sorted_words = [sorted(word) for word in words]
    # join the sorted words
    return " ".join(sorted_words)

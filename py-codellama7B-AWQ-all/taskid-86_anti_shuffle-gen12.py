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

    # list of words
    words = s.split()
    # list of ordered words
    ordered_words = []
    for word in words:
        # list of characters
        chars = list(word)
        # ordered list of characters
        ordered_chars = sorted(chars)
        # return word from ordered list of characters
        ordered_word = "".join(ordered_chars)
        # add to ordered_words list
        ordered_words.append(ordered_word)

    # return ordered string
    return " ".join(ordered_words)

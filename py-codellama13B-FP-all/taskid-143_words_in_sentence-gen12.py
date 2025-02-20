def words_in_sentence(sentence: str) -> str:
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
    >>> words_in_sentence('This is a test')
    'is'

    Example 2:
    >>> words_in_sentence('lets go for swimming')
    'go for'
    
    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """


    # solution
    sentence = sentence.split()
    new_sentence = []

    for word in sentence:
        if len(word) in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
            new_sentence.append(word)

    return ' '.join(new_sentence)

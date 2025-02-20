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

    # SOLUTION
    # create a set of prime numbers
    prime_set = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    # create an empty list to store the words
    words_list = list()
    # split the sentence into a list of words
    sentence_list = sentence.split(' ')
    # iterate through each word
    for word in sentence_list:
        # if the length of the word is prime
        if len(word) in prime_set:
            # add the word to the list
            words_list.append(word)
    # return the new string
    return ' '.join(words_list)

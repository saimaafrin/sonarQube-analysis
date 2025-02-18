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

    # Code here
    sentence_list = sentence.split()
    prime_list = []
    new_sentence = ""

    # check if word length is prime number
    for word in sentence_list:
        if is_prime(len(word)):
            prime_list.append(word)

    # combine new sentence
    for word in sentence_list:
        if word in prime_list:
            new_sentence += word + " "

    # remove extra space
    new_sentence = new_sentence[:-1]

    return new_sentence

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

    # create a list with all the words
    words = sentence.split(' ')
    # create an empty list to hold the prime numbers
    prime_numbers = []
    # iterate over each word
    for word in words:
        # check if the length of the word is a prime number
        if is_prime(len(word)):
            # if it is, append it to the list
            prime_numbers.append(word)
    # join the list using a space
    return ' '.join(prime_numbers)

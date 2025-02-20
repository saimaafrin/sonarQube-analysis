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

    # If the number of words in the sentence is 1 then return the word itself
    if sentence.count(' ') == 0:
        return sentence
    
    # The list to store the words whose lengths are prime numbers
    primes = []

    # Loop through the words in the sentence
    for word in sentence.split():
        # If the length of the word is prime add it to the list of primes
        if is_prime(len(word)):
            primes.append(word)
    
    # Return the list of words with their original order
    return ' '.join(primes)

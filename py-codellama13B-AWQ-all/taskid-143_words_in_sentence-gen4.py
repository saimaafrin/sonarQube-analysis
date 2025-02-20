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


    # Check if the input is a string
    if not isinstance(sentence, str):
        raise TypeError("Input should be a string")

    # Check if the input is not an empty string
    if sentence == "":
        raise ValueError("Input should not be an empty string")

    # Create a list of words in the sentence
    words_in_sentence = sentence.split(" ")

    # Create a list of prime numbers
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    # Create a list of words with prime numbers
    words_with_prime_numbers = [word for word in words_in_sentence if len(word) in prime_numbers]

    # Join the words with a space and return the result
    return " ".join(words_with_prime_numbers)

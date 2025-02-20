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

    # Use set comprehension to get the prime numbers from 2 to 31
    prime_numbers = {
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31
    }
    # Split sentence into words
    words = sentence.split()
    # Create a new list of words with prime lengths
    prime_words = [
        word for word in words if len(word) in prime_numbers
    ]
    # Join the words in the new list and return
    return ' '.join(prime_words)

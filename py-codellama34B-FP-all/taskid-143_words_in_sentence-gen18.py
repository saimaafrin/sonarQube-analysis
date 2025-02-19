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

    sentence_list = sentence.split()
    prime_numbers = []
    for word in sentence_list:
        length_of_word = len(word)
        if length_of_word > 1:
            for i in range(2, length_of_word):
                if length_of_word % i == 0:
                    break
            else:
                prime_numbers.append(word)

    return ' '.join(prime_numbers)


import random
import re

def task_func(target_words, n_sentences, vocabulary):
    """
    Generate sentences with spaces in certain target words replaced by underscores.

    Parameters:
    target_words (list of str): List of target words to replace spaces with underscores.
    n_sentences (int): Number of sentences to generate.
    vocabulary (list of str): List of words to sample from.

    Returns:
    list of str: A list of generated sentences in all lowercase, with specified words/phrases underscored.

    Raises:
    ValueError: If n_sentences is negative or if the vocabulary is empty.
    """
    if n_sentences < 0:
        raise ValueError("n_sentences must be non-negative")
    if not vocabulary:
        raise ValueError("vocabulary must not be empty")

    # Replace spaces in target words with underscores
    target_words = [re.sub(r"\s+", "_", word) for word in target_words]

    # Generate sentences with random words from vocabulary
    sentences = []
    for _ in range(n_sentences):
        sentence = " ".join(random.choices(vocabulary, k=10))
        sentences.append(sentence)

    # Replace spaces in target words in sentences
    for sentence in sentences:
        for word in target_words:
            sentence = sentence.replace(word, word.replace(" ", "_"))

    return sentences
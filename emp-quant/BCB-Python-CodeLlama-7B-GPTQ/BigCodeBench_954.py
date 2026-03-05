import random
import re
def task_func(target_words, n_sentences, vocabulary):
    """
    Generate sentences with spaces in certain target words replaced by underscores.

    Args:
        target_words (list of str): List of target words to be replaced by underscores.
        n_sentences (int): Number of sentences to generate.
        vocabulary (list of str): List of all possible words.

    Returns:
        list of str: A list of generated sentences in all lowercase, with specified words/phrases underscored.

    Raises:
        ValueError: If n_sentences is negative or if the vocabulary is empty.
    """
    if n_sentences < 0:
        raise ValueError("n_sentences must be non-negative")
    if not vocabulary:
        raise ValueError("vocabulary must not be empty")

    # Generate sentences with random words
    sentences = []
    for _ in range(n_sentences):
        sentence = " ".join(random.choices(vocabulary, k=10))
        sentences.append(sentence)

    # Replace spaces in target words with underscores
    for sentence in sentences:
        for word in target_words:
            sentence = re.sub(r"\b" + word + r"\b", word.replace(" ", "_"), sentence)

    return sentences
target_words = ["hello", "world"]
vocabulary = ["hello", "world", "python", "is", "a", "great", "language"]
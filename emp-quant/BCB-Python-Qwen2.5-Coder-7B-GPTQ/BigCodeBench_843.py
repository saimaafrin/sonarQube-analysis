import random
import re
WORD_LIST = ["sample", "text", "contains", "several", "words", "including"]
def task_func(n_sentences):
    """
    Generates a string of random sentences using a predefined word list.
    
    Parameters:
    n_sentences (int): The number of sentences to generate.
    
    Returns:
    str: A string containing the generated sentences in lowercase, with non-alphanumeric characters removed (except for single periods ending sentences).
    """
    sentences = []
    for _ in range(n_sentences):
        # Randomly select words to form a sentence
        words = random.sample(WORD_LIST, random.randint(1, 5))
        sentence = ' '.join(words) + '.'
        sentences.append(sentence)
    
    # Concatenate all sentences into one string
    result = ' '.join(sentences)
    
    # Remove non-alphanumeric characters except spaces and periods
    result = re.sub(r'[^a-zA-Z0-9 .]', '', result)
    
    # Convert to lowercase
    result = result.lower()
    
    return result
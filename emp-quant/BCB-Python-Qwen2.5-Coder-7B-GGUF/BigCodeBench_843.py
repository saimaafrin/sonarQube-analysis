
import random
import re

# Constants
WORD_LIST = ["sample", "text", "contains", "several", "words", "including"]

def task_func(n_sentences):
    def generate_sentence():
        num_words = random.randint(1, 10)  # Random number of words between 1 and 10
        sentence = ' '.join(random.choices(WORD_LIST, k=num_words))
        return sentence.capitalize() + '.'

    sentences = [generate_sentence() for _ in range(n_sentences)]
    result = ' '.join(sentences)
    result = re.sub(r'[^a-zA-Z0-9. ]', '', result)  # Remove non-alphanumeric characters except periods and spaces
    return result.lower()
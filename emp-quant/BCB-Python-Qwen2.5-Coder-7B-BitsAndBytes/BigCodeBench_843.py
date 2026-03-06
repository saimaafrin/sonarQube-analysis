
import random
import re

# Constants
WORD_LIST = ["sample", "text", "contains", "several", "words", "including"]

def task_func(n_sentences):
    def generate_sentence():
        num_words = random.randint(1, 10)  # Random number of words between 1 and 10
        sentence = ' '.join(random.choices(WORD_LIST, k=num_words))
        return sentence.capitalize() + '.'  # Capitalize the first letter and add a period

    sentences = [generate_sentence() for _ in range(n_sentences)]
    result_string = ' '.join(sentences).lower()
    cleaned_string = re.sub(r'[^a-z .]', '', result_string)
    return cleaned_string.strip()
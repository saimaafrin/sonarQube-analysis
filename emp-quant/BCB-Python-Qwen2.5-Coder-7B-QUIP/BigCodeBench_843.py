
import random
import re
# Constants
WORD_LIST = ["sample", "text", "contains", "several", "words", "including"]

def task_func(n_sentences):
    # Helper function to generate a random sentence
    def generate_sentence():
        num_words = random.randint(3, 10)  # Random number of words between 3 and 10
        sentence = ' '.join(random.sample(WORD_LIST, num_words))  # Select random words from the list
        return sentence.capitalize() + '.'  # Add a period at the end

    # Generate n sentences
    sentences = [generate_sentence() for _ in range(n_sentences)]

    # Concatenate all sentences into a single string
    full_text = ''.join(sentences)

    # Remove non-alphanumeric characters except for spaces and periods
    cleaned_text = re.sub(r'[^a-zA-Z0-9 .]', '', full_text)

    # Convert to lowercase
    result = cleaned_text.lower()

    return result
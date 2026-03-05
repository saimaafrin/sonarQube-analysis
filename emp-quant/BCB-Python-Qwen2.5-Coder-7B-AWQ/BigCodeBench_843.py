import random
import re
WORD_LIST = ["sample", "text", "contains", "several", "words", "including"]
def task_func(n_sentences):
    # Helper function to generate a single random sentence
    def generate_sentence():
        num_words = random.randint(1, 10)  # Random number of words between 1 and 10
        sentence = ' '.join(random.choices(WORD_LIST, k=num_words))
        return sentence.capitalize() + '.'
    
    # Generate n_sentences
    sentences = [generate_sentence() for _ in range(n_sentences)]
    
    # Concatenate sentences into a single string
    result = ' '.join(sentences)
    
    # Remove non-alphanumeric characters except for single periods
    result = re.sub(r'[^a-zA-Z0-9. ]', '', result)
    
    # Convert to lowercase
    result = result.lower()
    
    return result
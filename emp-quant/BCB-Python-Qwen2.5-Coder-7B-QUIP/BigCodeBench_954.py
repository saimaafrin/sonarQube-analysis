
import random
import re

def task_func(target_words, n_sentences, vocabulary):
    if n_sentences < 0 or not vocabulary:
        raise ValueError("Invalid input: n_sentences must be non-negative and vocabulary must not be empty")
    
    # Ensure target_words is a list of strings
    if not isinstance(target_words, list):
        target_words = [target_words]
    
    # Ensure vocabulary is a list of strings
    if not isinstance(vocabulary, list):
        vocabulary = [vocabulary]
    
    # Create a list to hold the generated sentences
    sentences = []
    
    # Generate n_sentences sentences
    for _ in range(n_sentences):
        # Randomly sample 10 words with replacement from the vocabulary
        sentence_words = random.choices(vocabulary, k=10)
        
        # Join the words with a single whitespace
        sentence = ' '.join(sentence_words)
        
        # Replace spaces within target words with underscores
        for word in target_words:
            sentence = re.sub(r'\b' + re.escape(word) + r'\b', word.replace(' ', '_'), sentence, flags=re.IGNORECASE)
        
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        
        # Add the processed sentence to the list
        sentences.append(sentence)
    
    return sentences

import re
import matplotlib.pyplot as plt
from nltk.probability import FreqDist

def task_func(example_str, top_n=30):
    # Extract text not enclosed in square brackets
    pattern = r'\[(.*?)\]'
    cleaned_text = re.sub(pattern, '', example_str)
    
    # Tokenize the text into words
    words = cleaned_text.split()
    
    # Create a frequency distribution of the words
    freq_dist = FreqDist(words)
    
    # Get the top_n most common words
    top_words = freq_dist.most_common(top_n)
    
    # Plot the frequency distribution
    fig, ax = plt.subplots()
    ax.bar([word for word, freq in top_words], [freq for word, freq in top_words])
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Top {} Most Common Words'.format(top_n))
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return ax, dict(top_words)

print("Top", len(top_words_dict), "most common words:", top_words_dict)
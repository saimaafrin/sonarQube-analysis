import collections
import matplotlib.pyplot as plt
import pandas as pd
def task_func(sentences_dict, word_keys):
    # Initialize a dictionary to store word frequencies
    word_freq = collections.defaultdict(int)
    
    # Iterate over each sentence in the dictionary
    for sentences in sentences_dict.values():
        # Split the sentence into words and count occurrences
        for word in sentences.split():
            if word in word_keys:
                word_freq[word] += 1
    
    # Create a DataFrame from the word frequencies
    df = pd.DataFrame(list(word_freq.items()), columns=['Word', 'Frequency'])
    
    # Sort the DataFrame by frequency in descending order
    df = df.sort_values(by='Frequency', ascending=False)
    
    # Create a bar chart using matplotlib
    fig, ax = plt.subplots()
    ax.bar(df['Word'], df['Frequency'], color='blue')
    
    # Set the title and labels
    ax.set_title('Word Frequencies')
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    
    # Rotate the x-axis labels for better readability
    ax.set_xticklabels(df['Word'], rotation=45)
    
    # Return the Axes object
    return ax
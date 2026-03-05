
import matplotlib.pyplot as plt
import random
import string
import pandas as pd
import seaborn as sns
# Constants
LETTERS = list(string.ascii_lowercase)

def task_func(rows=1000, string_length=3):
    """
    Generates a dataframe of random strings and creates a heatmap showing the correlation in the frequency of each letter.
    
    Parameters:
    rows (int): The number of random strings to generate.
    string_length (int): The length of each string.
    
    Returns:
    matplotlib.axes._subplots.AxesSubplot or None: A seaborn heatmap plot object if data is generated; otherwise, None.
    """
    if rows == 0:
        print("No data to generate heatmap.")
        return None
    
    # Generate random strings
    strings = [''.join(random.choices(LETTERS, k=string_length)) for _ in range(rows)]
    
    # Create a DataFrame from the list of strings
    df = pd.DataFrame(strings, columns=['string'])
    
    # Split each string into its constituent letters and create a one-hot encoded DataFrame
    letter_counts = {}
    for letter in LETTERS:
        letter_counts[letter] = df['string'].str.count(letter).astype(int)
    
    # Sum the one-hot encoded values to get the frequency of each letter
    letter_freq = letter_counts.sum(axis=0)
    
    # Create a heatmap
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(letter_freq.values.reshape(1, -1), annot=True, cmap='viridis')
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Heatmap of Letter Frequency')
    plt.show()
    
    return heatmap
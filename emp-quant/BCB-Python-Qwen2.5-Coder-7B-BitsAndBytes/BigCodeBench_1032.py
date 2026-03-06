
import matplotlib.pyplot as plt
import random
import string
import pandas as pd
import seaborn as sns

# Constants
LETTERS = list(string.ascii_lowercase)

def task_func(rows=1000, string_length=3):
    """
    Generates a dataframe of random strings and creates a heatmap showing the correlation 
    in the frequency of each letter in these strings.

    Parameters:
    rows (int): The number of random strings to generate.
    string_length (int): The length of each random string.

    Returns:
    matplotlib.axes._axes.Axes or None: A seaborn heatmap plot object if data is generated; otherwise, None.
    """
    if rows == 0:
        print("No data to generate heatmap.")
        return None
    
    # Generate random strings
    data = [''.join(random.choices(LETTERS, k=string_length) for _ in range(rows)) for _ in range(rows)]
    df = pd.DataFrame(data)
    
    # Convert strings to one-hot encoding
    one_hot_encoded = pd.get_dummies(df.applymap(lambda x: [x[i] for i in range(len(x))]))
    
    # Sum up the encodings to get the frequency of each letter
    letter_frequency = one_hot_encoded.sum()
    
    # Create a correlation matrix
    correlation_matrix = letter_frequency.corr()
    
    # Plot the heatmap
    plt.figure(figsize=(12, 8))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
    plt.title('Correlation Heatmap of Letter Frequencies')
    plt.show()
    
    return heatmap
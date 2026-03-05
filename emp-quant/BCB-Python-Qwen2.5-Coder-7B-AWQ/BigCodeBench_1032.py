import matplotlib.pyplot as plt
import random
import string
import pandas as pd
import seaborn as sns
LETTERS = list(string.ascii_lowercase)
def task_func(rows=1000, string_length=3):
    """
    Generates a dataframe of random strings and creates a heatmap showing the correlation in the frequency of each letter.
    
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
    data = [''.join(random.choices(LETTERS, k=string_length)) for _ in range(rows)]
    df = pd.DataFrame(data, columns=['String'])
    
    # Convert strings to one-hot encoded format
    one_hot = pd.get_dummies(df['String'].str.split('', expand=True).stack()).groupby(level=0).sum()
    
    # Calculate correlation matrix
    correlation_matrix = one_hot.corr()
    
    # Create heatmap
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap of Letter Frequencies')
    plt.show()
    
    return heatmap
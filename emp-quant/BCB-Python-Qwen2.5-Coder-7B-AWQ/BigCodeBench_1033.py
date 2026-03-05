import itertools
import string
import pandas as pd
import matplotlib.pyplot as plt
def task_func():
    # Generate all possible 3-letter combinations
    letters = string.ascii_lowercase
    combinations = list(itertools.product(letters, repeat=3))
    
    # Create a DataFrame from these combinations
    df = pd.DataFrame(combinations, columns=['First', 'Second', 'Third'])
    
    # Plot a histogram of the frequency of the first letters
    ax = df['First'].value_counts().plot(kind='bar')
    ax.set_xlabel('First Letter')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of First Letters in 3-Letter Combinations')
    
    return (df, ax)
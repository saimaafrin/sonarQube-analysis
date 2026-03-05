import itertools
import string
import pandas as pd
import matplotlib.pyplot as plt
def task_func():
    # Generate all possible 3-letter combinations
    letters = string.ascii_lowercase
    combinations = list(itertools.product(letters, repeat=3))
    
    # Create a DataFrame from the combinations
    df = pd.DataFrame(combinations, columns=['First', 'Second', 'Third'])
    
    # Plot a histogram of the frequency of the first letters
    ax = df['First'].value_counts().plot(kind='bar')
    
    return df, ax
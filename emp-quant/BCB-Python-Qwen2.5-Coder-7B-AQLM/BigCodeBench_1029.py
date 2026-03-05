
import pandas as pd
import numpy as np

def task_func(rows=100, columns=3):
    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Create a DataFrame with random alphabets
    data = np.random.choice(list(alphabet), size=(rows, columns))
    df = pd.DataFrame(data, columns=[chr(97 + i) for i in range(columns)])
    
    return df

import pandas as pd
import numpy as np

def task_func(rows=100, columns=3):
    # Create a list of lowercase letters from 'a' to 'z'
    alphabet = [chr(i) for i in range(97, 123)]
    
    # Generate a DataFrame with random alphabets
    data = np.random.choice(alphabet, size=(rows, columns))
    df = pd.DataFrame(data, columns=[chr(i) for i in range(97, 97 + columns)])
    
    return df

import pandas as pd
import numpy as np

def task_func(rows=100, columns=3):
    # Create a list of random alphabets
    alphabet_list = np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), size=rows)

    # Create a DataFrame with the random alphabets
    df = pd.DataFrame(alphabet_list, columns=['a', 'b', 'c'])

    # Return the DataFrame
    return df
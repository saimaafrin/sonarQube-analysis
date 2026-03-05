import pandas as pd
import numpy as np
def task_func(rows=100, columns=3):
    # Generate random alphabets for each cell
    data = np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), size=(rows, columns))
    # Create DataFrame with the generated data
    df = pd.DataFrame(data, columns=[chr(i) for i in range(97, 97 + columns)])
    return df
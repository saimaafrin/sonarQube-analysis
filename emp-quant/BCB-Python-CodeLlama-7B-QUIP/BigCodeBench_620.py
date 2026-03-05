
import numpy as np
import pandas as pd

# Constants
RANGE = (1, 100)

def task_func(L):
    # Initialize the DataFrame with random integers
    df = pd.DataFrame(np.random.randint(RANGE[0], RANGE[1], size=(L[0] * L[1], L[2] * L[3])))
    return df
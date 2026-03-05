from random import shuffle
import pandas as pd
import numpy as np
def task_func(l, n_groups = 5):
    # Shuffle the list
    shuffle(l)

    # Construct a DataFrame from the shuffled list
    df = pd.DataFrame(l)

    # Move the first n_groups elements to the end of each row
    for i in range(n_groups):
        df.iloc[i] = df.iloc[i].append(df.iloc[i].iloc[i])

    return df
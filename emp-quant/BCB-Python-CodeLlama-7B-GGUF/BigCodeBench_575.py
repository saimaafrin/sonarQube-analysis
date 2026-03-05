
from random import shuffle
import pandas as pd
import numpy as np

# Constants
n_groups = 5

# Shuffle the list
shuffled_list = shuffle(l)

# Construct a DataFrame from the shuffled list
df = pd.DataFrame(shuffled_list)

# Move the first n_groups elements to the end of each row
for i in range(n_groups):
    df.iloc[i, :] = df.iloc[i, -n_groups:]
    df.iloc[i, -n_groups:] = df.iloc[i, :n_groups]

# Output the modified DataFrame
print(df)
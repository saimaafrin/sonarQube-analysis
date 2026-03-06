
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(rows):
    # Create a DataFrame with random integers between 0 and 9
    data = {col: np.random.randint(0, 10, rows) for col in COLUMNS}
    df = pd.DataFrame(data)
    
    # Count the non-zero values in each column
    non_zero_counts = df.count()
    
    # Visualize the information using a bar plot
    fig, ax = plt.subplots()
    non_zero_counts.plot(kind='bar', ax=ax)
    ax.set_xlabel('Columns')
    ax.set_ylabel('Non-Zero Values')
    ax.set_title('Count of Non-Zero Values in Each Column')
    
    return df, ax

import pandas as pd
import matplotlib.pyplot as plt
COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    # Create the DataFrame from the input data
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Group the DataFrame by the first COLUMNS[-1] columns and calculate the mean of the last column
    grouped_df = df.groupby(df.columns[:-1]).mean().reset_index()
    
    # Create the line chart
    fig, ax = plt.subplots()
    for i, row in grouped_df.iterrows():
        ax.plot([i], row[COLUMNS[-1]], 'o')
    
    # Set the labels
    ax.set_xlabel('-'.join(COLUMNS[:-1]))
    ax.set_ylabel(COLUMNS[-1])
    
    return grouped_df, ax
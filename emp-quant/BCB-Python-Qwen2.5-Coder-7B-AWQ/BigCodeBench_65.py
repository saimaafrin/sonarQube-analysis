import pandas as pd
import matplotlib.pyplot as plt
COLUMNS = ['col1', 'col2', 'col3']
def task_func(data):
    # Create a DataFrame from the input data
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Group the DataFrame by all columns except the last one
    grouped = df.groupby(df.columns[:-1]).size().reset_index(name='count')
    
    # Create a line chart
    fig, ax = plt.subplots()
    for name, group in grouped.groupby(COLUMNS[:-1]):
        ax.plot(group[COLUMNS[-1]], group['count'], label='-'.join(map(str, name)))
    
    # Set labels
    ax.set_xlabel('-'.join(COLUMNS[:-1]))
    ax.set_ylabel(COLUMNS[-1])
    
    # Add legend
    ax.legend()
    
    return df, ax
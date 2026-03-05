
import pandas as pd
import matplotlib.pyplot as plt

# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def task_func(data):
    # Convert the input data to a pandas DataFrame
    df = pd.DataFrame(data, columns=COLUMN_NAMES)
    
    # Calculate the average of each row
    row_averages = df.mean(axis=1)
    
    # Append the row averages as a new column
    df['Average'] = row_averages
    
    # Plot the row averages
    fig, ax = plt.subplots()
    ax.plot(df.index, df['Average'], marker='o')
    ax.set_xlabel('Row Index')
    ax.set_ylabel('Row Average')
    ax.set_title('Row Averages')
    
    return df, ax
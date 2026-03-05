
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df, target_values=[1, 3, 4]):
    # Replace elements not in target_values with zero
    for column in df.columns:
        df[column] = df[column].apply(lambda x: x if x in target_values else 0)
    
    # Plot the distribution of each column
    for column in df.columns:
        plt.figure()
        sns.histplot(df[column], kde=True)
        plt.title(f'Distribution of {column}')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df, target_values=[1, 3, 4]):
    # Replace values not in target_values with 0
    for column in df.columns:
        df[column] = df[column].apply(lambda x: x if x in target_values else 0)
    
    # Plot distribution of each column
    fig, axes = plt.subplots(nrows=len(df.columns), ncols=1, figsize=(10, 20))
    
    for i, column in enumerate(df.columns):
        sns.histplot(df[column], ax=axes[i], kde=True)
        axes[i].set_title(f'Distribution of {column}')
        axes[i].set_xlabel(column)
        axes[i].set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()
    
    return axes
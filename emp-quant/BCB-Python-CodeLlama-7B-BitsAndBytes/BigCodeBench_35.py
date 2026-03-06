
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df, target_values=[1, 3, 4]):
    # Replace all elements in DataFrame columns that do not exist in the target_values array with zeros
    for col in df.columns:
        df[col] = df[col].apply(lambda x: 0 if x not in target_values else x)

    # Output the distribution of each column after replacing
    for col in df.columns:
        sns.distplot(df[col], label=col)
        plt.legend()

    # Return the Axes object of the plotted data
    return plt.gca()
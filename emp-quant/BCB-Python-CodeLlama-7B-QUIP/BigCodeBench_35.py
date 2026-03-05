
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df, target_values):
    # Replace all elements in DataFrame columns that do not exist in the target_values array with zeros
    for col in df.columns:
        df[col] = df[col].apply(lambda x: 0 if x not in target_values else x)

    # Plot the distribution of each column after replacing
    for col in df.columns:
        plt.subplot(111)
        sns.distplot(df[col], label=col)
        plt.title(col)

    plt.show()
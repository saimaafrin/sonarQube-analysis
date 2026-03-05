import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df, target_values=[1, 3, 4]):
    """
    Replace all elements in DataFrame columns that do not exist in the target_values array with zeros, and then output the distribution of each column after replacing.
    """
    # Replace all elements in DataFrame columns that do not exist in the target_values array with zeros
    for col in df.columns:
        df[col] = df[col].replace(to_replace=df[col].unique().difference(target_values), value=0)

    # Output the distribution of each column after replacing
    fig, axs = plt.subplots(nrows=len(df.columns), ncols=1, figsize=(10, 10))
    for i, col in enumerate(df.columns):
        sns.distplot(df[col], ax=axs[i])
        axs[i].set_title(col)
    return axs
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [1, 2, 3, 4, 5],
    'C': [1, 2, 3, 4, 5],
    'D': [1, 2, 3, 4, 5],
})
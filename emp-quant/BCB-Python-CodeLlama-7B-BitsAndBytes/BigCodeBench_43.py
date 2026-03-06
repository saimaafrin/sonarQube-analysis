
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df):
    # Replace NaN values with the average of the column
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df[col].fillna(df[col].mean(), inplace=True)

    # Calculate statistics for each numeric column
    stats = df.describe()

    # Create distribution plots for each numeric column
    fig, axs = plt.subplots(nrows=len(df.select_dtypes(include=['float64', 'int64']).columns), ncols=1, figsize=(10, 10))
    for i, col in enumerate(df.select_dtypes(include=['float64', 'int64']).columns):
        sns.distplot(df[col], ax=axs[i])

    return (stats, axs)

stats, axs = task_func(df)
print(stats)
print(axs)
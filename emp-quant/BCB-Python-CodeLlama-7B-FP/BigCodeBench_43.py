import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
def task_func(df):
    # Replace NaN values with the average of the column
    df = df.fillna(df.mean())

    # Calculate statistics for each numeric column
    stats = df.describe()

    # Create distribution plots for each numeric column
    fig, axs = plt.subplots(nrows=len(df.select_dtypes(include=np.number).columns), ncols=1, figsize=(10, 10))
    for i, col in enumerate(df.select_dtypes(include=np.number).columns):
        sns.distplot(df[col], ax=axs[i], bins=10)

    return (stats, axs)
df = pd.DataFrame({'A': [1, 2, 3, 4, 5, np.nan],
                   'B': [10, 20, 30, 40, 50, np.nan],
                   'C': [100, 200, 300, 400, 500, np.nan]})
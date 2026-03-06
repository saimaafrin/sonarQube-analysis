
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def task_func(dataframe, target_value='332'):
    # Create a DataFrame with Boolean values indicating the presence of the target value
    bool_df = dataframe.eq(target_value).astype(int)

    # Create a heatmap of the Boolean DataFrame
    ax = sns.heatmap(bool_df, cmap='coolwarm')

    # Return the Axes object of the heatmap and the Boolean DataFrame
    return ax, bool_df

# Visualize the heatmap
plt.show()
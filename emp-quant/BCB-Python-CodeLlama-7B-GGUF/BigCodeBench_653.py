
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def task_func(dataframe, target_value='332'):
    # Create a DataFrame with Boolean values indicating the presence of the target value
    target_mask = dataframe.eq(target_value)

    # Visualize the heatmap
    ax = sns.heatmap(target_mask, cmap='Reds')

    return target_mask, ax

# Call the function
result = task_func(dataframe, target_value)

# Print the resulting DataFrame and Axes object
print(result[0])
print(result[1])
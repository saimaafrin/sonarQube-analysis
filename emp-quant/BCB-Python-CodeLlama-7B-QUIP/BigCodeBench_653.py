
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(dataframe, target_value='332'):
    # Create a DataFrame with Boolean values indicating the presence of the target value in the input DataFrame
    presence_df = dataframe.apply(lambda x: x == target_value)

    # Create a heatmap of the DataFrame
    ax = sns.heatmap(presence_df, cmap='viridis')

    # Set the title of the heatmap
    ax.set_title('Heatmap of presence of target value in DataFrame')

    # Set the x-axis label
    ax.set_xlabel('Column index')

    # Set the y-axis label
    ax.set_ylabel('Row index')

    # Set the colorbar label
    ax.set_colorbar('Presence of target value')

    # Return the heatmap
    return ax
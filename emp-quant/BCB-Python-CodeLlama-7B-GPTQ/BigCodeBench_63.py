import pandas as pd
import matplotlib.pyplot as plt
def task_func(car_dict):
    """
    Create a DataFrame with car brands and their colors, and visualize the distribution of vehicle colors in a bar chart.

    Parameters
    ----------
    car_dict : dict
        A dictionary of car brands and their corresponding colors.

    Returns
    -------
    tuple
        A tuple containing:

        DataFrame: A pandas DataFrame with car brands and their colors.
        Axes: The Axes object of the bar chart visualizing the distribution of vehicle colors.
    """
    # Create a DataFrame with car brands and their colors
    df = pd.DataFrame(car_dict, columns=['Car', 'Color'])

    # Visualize the distribution of vehicle colors in a bar chart
    fig, ax = plt.subplots()
    ax.bar(df['Color'].value_counts().index, df['Color'].value_counts().values)
    ax.set_title('Distribution of Vehicle Colors')
    ax.set_xlabel('Vehicle Color')
    ax.set_ylabel('Count')

    return df, ax
car_dict = {'Toyota': 'Red', 'Honda': 'Blue', 'Ford': 'Green', 'Chevrolet': 'Black', 'Nissan': 'White'}
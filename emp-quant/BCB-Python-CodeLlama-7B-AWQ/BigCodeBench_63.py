import pandas as pd
import matplotlib.pyplot as plt
def task_func(car_dict):
    """
    Create a DataFrame with car brands and their colors and visualize the distribution of vehicle colors in a bar chart.

    Parameters
    ----------
    car_dict : dict
        A dictionary of car brands as keys and their colors as values.

    Returns
    -------
    tuple
        A tuple containing:

        DataFrame: A pandas DataFrame with car brands and their colors.
        Axes: The Axes object of the bar chart visualizing the distribution of vehicle colors.
    """
    # Create a DataFrame with car brands and their colors
    df = pd.DataFrame.from_dict(car_dict, orient='index')
    df.columns = ['Color']

    # Visualize the distribution of vehicle colors in a bar chart
    ax = df['Color'].value_counts().plot(kind='bar', title='Distribution of Vehicle Colors')

    return df, ax
car_dict = {'Toyota': 'Red', 'Honda': 'Blue', 'Ford': 'Green', 'Chevrolet': 'Black', 'Nissan': 'White'}
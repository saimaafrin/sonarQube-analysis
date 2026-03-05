
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data):
    # Check if input data is a 2D array and contains only numeric data
    if not isinstance(data, pd.DataFrame) or not data.apply(lambda x: isinstance(x, (int, float))).all().all():
        raise ValueError("Input data must be a 2D array of numeric values")

    # Calculate the average of values across each row
    data['Average'] = data.apply(lambda x: x.mean(), axis=1)

    # Create a correlation matrix and visualize it as a heatmap
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')

    # Return the DataFrame and the Axes object
    return data, plt.gca()
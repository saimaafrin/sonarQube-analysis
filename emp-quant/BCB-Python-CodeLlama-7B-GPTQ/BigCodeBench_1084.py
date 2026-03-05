import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_selection import f_oneway
def task_func(data_file_path: str):
    # Read the CSV file
    data = pd.read_csv(data_file_path)

    # Convert string representations of numbers with commas into floating point numbers
    data = data.apply(pd.to_numeric, errors='coerce')

    # Calculate the mean and standard deviation for each numerical column
    means = data.mean(axis=0)
    std_devs = data.std(axis=0)

    # Generate a histogram plot for each numerical column
    axes = []
    for col in data.columns:
        if data[col].dtype == np.float64:
            ax = data[col].plot.hist(bins=20)
            axes.append(ax)

    # Perform an ANOVA test to check the statistical significance of differences between means of numerical columns (if applicable)
    anova_results = None
    if len(data.columns) > 1:
        anova_results = f_oneway(data.iloc[:, :-1], data.iloc[:, -1])

    # Output with:
    # means (pd.Series): Mean values of each numerical column.
    # std_devs (pd.Series): Standard deviation values of each numerical column.
    # axes (list[matplotlib.axes.Axes]): List of histogram plots for each numerical column.
    # anova_results (pd.DataFrame): ANOVA test results for each pair of numerical columns (if more than one numerical column is present).
    return means, std_devs, axes, anova_results
data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15]})
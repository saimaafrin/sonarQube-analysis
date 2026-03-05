import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_selection import f_oneway
def task_func(data_file_path: str):
    # Read the CSV file
    data = pd.read_csv(data_file_path)

    # Convert string representations of numbers with commas into floating point numbers
    data = data.apply(lambda x: x.astype(float) if x.dtype == 'object' else x)

    # Calculate the mean and standard deviation for each numerical column
    means = data.mean(axis=0)
    std_devs = data.std(axis=0)

    # Generate a histogram plot for each numerical column
    axes = []
    for col in data.columns:
        if data[col].dtype == 'float64':
            ax = data[col].plot.hist(bins=50, alpha=0.5, label=col)
            axes.append(ax)

    # Perform an ANOVA test to check the statistical significance of differences between means of numerical columns (if applicable)
    anova_results = None
    if len(data.columns) > 1:
        anova_results = f_oneway(data.iloc[:, 0], data.iloc[:, 1])

    # Compute two columns "F-value" and "P-value" for each pair of numerical columns
    f_values = anova_results.fvalue if anova_results is not None else None
    p_values = anova_results.pvalue if anova_results is not None else None

    return means, std_devs, axes, anova_results, f_values, p_values
data_file_path = 'data.csv'
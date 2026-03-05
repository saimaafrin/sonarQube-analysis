import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_selection import f_oneway
def task_func(data_file_path: str):
    # Read the CSV file
    df = pd.read_csv(data_file_path)

    # Convert string representations of numbers with commas into floating point numbers
    df = df.apply(lambda x: x.str.replace(',', '').astype(float))

    # Calculate the mean and standard deviation for each numerical column
    means = df.select_dtypes(include=['number']).mean()
    std_devs = df.select_dtypes(include=['number']).std()

    # Generate a histogram plot for each numerical column
    axes = []
    for col in df.select_dtypes(include=['number']).columns:
        ax = df[col].plot.hist(bins=50, alpha=0.5, label=col)
        axes.append(ax)

    # Perform an ANOVA test to check the statistical significance of differences between means of numerical columns (if applicable)
    if len(df.select_dtypes(include=['number']).columns) > 1:
        anova_results = f_oneway(df.select_dtypes(include=['number']).columns)
        anova_results['F-value'] = anova_results['F-value'].apply(lambda x: round(x, 2))
        anova_results['P-value'] = anova_results['P-value'].apply(lambda x: round(x, 2))
    else:
        anova_results = None

    return means, std_devs, axes, anova_results
data_file_path = 'data.csv'
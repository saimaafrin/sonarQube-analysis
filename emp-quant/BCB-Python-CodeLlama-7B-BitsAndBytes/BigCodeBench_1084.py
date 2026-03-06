
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import f_oneway

def task_func(data_file_path: str):
    # Read the CSV file and convert string representations of numbers with commas into floating point numbers
    df = pd.read_csv(data_file_path)
    df = df.apply(pd.to_numeric, errors='coerce')

    # Calculate the mean and standard deviation for each numerical column
    means = df.mean()
    std_devs = df.std()

    # Generate a histogram plot for each numerical column
    axes = []
    for col in df.columns:
        if df[col].dtype == 'float64':
            ax = df[col].hist(bins=50, alpha=0.5, label=col)
            axes.append(ax)

    # Perform an ANOVA test to check the statistical significance of differences between means of numerical columns (if applicable)
    anova_results = None
    if len(df.columns) > 1:
        anova_results = f_oneway(df.iloc[:, :-1], df.iloc[:, -1])

    # Output the results
    return means, std_devs, axes, anova_results
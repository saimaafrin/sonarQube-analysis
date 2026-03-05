
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import f_oneway

def task_func(data_file_path: str):
    # Read CSV file
    df = pd.read_csv(data_file_path)

    # Convert string representations of numbers with commas into floating point numbers
    df = df.apply(pd.to_numeric, errors='coerce')

    # Calculate mean and standard deviation for each numerical column
    means = df.mean()
    std_devs = df.std()

    # Generate histogram plots for each numerical column
    axes = []
    for col in df.columns:
        if df[col].dtype == 'float64':
            ax = df[col].hist(bins=50)
            axes.append(ax)

    # Perform ANOVA test to check the statistical significance of differences between means of numerical columns (if applicable)
    anova_results = None
    if len(df.columns) > 1:
        anova_results = f_oneway(df)

    # Output
    return means, std_devs, axes, anova_results
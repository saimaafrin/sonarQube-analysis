
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import f_oneway

def task_func(data_file_path: str):
    # Read the CSV file
    data = pd.read_csv(data_file_path)

    # Convert string representations of numbers to floating point numbers
    data = data.apply(lambda x: x.replace(',', '.') if x.dtype == 'object' else x)

    # Calculate the mean and standard deviation for each numerical column
    means = data.mean()
    std_devs = data.std()

    # Generate histogram plots for each numerical column
    axes = []
    for col in data.columns:
        ax = plt.hist(data[col], bins=50)
        axes.append(ax)

    # Perform ANOVA test for each pair of numerical columns
    if len(data.columns) > 1:
        anova_results = f_oneway(data)
        anova_results.rename(columns={'F-value': 'F-value', 'P-value': 'P-value'}, inplace=True)

    return means, std_devs, axes, anova_results
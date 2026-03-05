
import pandas as pd
from sklearn.feature_selection import f_oneway
import matplotlib.pyplot as plt

def task_func(data_file_path: str):
    # Read the CSV file
    data = pd.read_csv(data_file_path)
    
    # Convert string representations of numbers with commas to floating point numbers
    data = data.apply(pd.to_numeric, errors='coerce')
    
    # Calculate the mean and standard deviation for each numerical column
    means = data.mean()
    std_devs = data.std()
    
    # Generate a histogram plot for each numerical column
    axes = []
    for column in data.columns:
        fig, ax = plt.subplots()
        data[column].plot(kind='hist', ax=ax)
        axes.append(ax)
    
    # Perform an ANOVA test to check the statistical significance of differences between means of numerical columns
    anova_results = pd.DataFrame()
    if len(data.columns) > 1:
        for i in range(len(data.columns)):
            for j in range(i+1, len(data.columns)):
                f_value, p_value = f_oneway(data.iloc[:, i], data.iloc[:, j])
                anova_results = anova_results.append(pd.DataFrame({'Feature1': data.columns[i], 'Feature2': data.columns[j], 'F-value': f_value, 'P-value': p_value}), ignore_index=True)
    
    return means, std_devs, axes, anova_results
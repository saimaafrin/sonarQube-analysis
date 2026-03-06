
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from sklearn.feature_selection import f_oneway

def task_func(data_file_path: str):
    # Read the CSV file
    df = pd.read_csv(data_file_path)
    
    # Convert string representations of numbers with commas into floating point numbers
    df.replace(',', '', regex=True, inplace=True)
    df = df.astype(float)
    
    # Calculate the mean and standard deviation for each numerical column
    means = df.mean()
    std_devs = df.std()
    
    # Generate a histogram plot for each numerical column
    fig, axes = plt.subplots(len(df.columns), 1, figsize=(10, len(df.columns)*4))
    for i, col in enumerate(df.columns):
        axes[i].hist(df[col], bins=30)
        axes[i].set_title(f'Histogram of {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Frequency')
    
    # Perform an ANOVA test to check the statistical significance of differences between means of numerical columns
    anova_results = None
    if len(df.columns) > 1:
        anova_results = pd.DataFrame(columns=['Column1', 'Column2', 'F-value', 'P-value'])
        for i in range(len(df.columns)):
            for j in range(i+1, len(df.columns)):
                f_value, p_value = f_oneway(df.iloc[:, i], df.iloc[:, j])
                anova_results = anova_results.append({'Column1': df.columns[i], 'Column2': df.columns[j], 'F-value': f_value, 'P-value': p_value}, ignore_index=True)
    
    return means, std_devs, axes, anova_results
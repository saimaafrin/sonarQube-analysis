import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import f_oneway
def task_func(data_file_path: str):
    # Read the CSV file
    data = pd.read_csv(data_file_path)
    
    # Convert string representations of numbers with commas into floating point numbers
    data = data.apply(pd.to_numeric, errors='coerce')
    
    # Calculate the mean and standard deviation for each numerical column
    means = data.mean()
    std_devs = data.std()
    
    # Generate a histogram plot for each numerical column
    axes = []
    for column in data.columns:
        if pd.api.types.is_numeric_dtype(data[column]):
            fig, ax = plt.subplots()
            data[column].hist(ax=ax)
            ax.set_title(f'Histogram of {column}')
            ax.set_xlabel(column)
            ax.set_ylabel('Frequency')
            axes.append(ax)
    
    # Perform an ANOVA test to check the statistical significance of differences between means of numerical columns
    anova_results = pd.DataFrame(columns=['Column1', 'Column2', 'F-value', 'P-value'])
    if len(data.columns) > 1:
        for i in range(len(data.columns)):
            for j in range(i + 1, len(data.columns)):
                column1 = data.columns[i]
                column2 = data.columns[j]
                if pd.api.types.is_numeric_dtype(data[column1]) and pd.api.types.is_numeric_dtype(data[column2]):
                    f_value, p_value = f_oneway(data[column1], data[column2])
                    anova_results = anova_results.append({'Column1': column1, 'Column2': column2, 'F-value': f_value, 'P-value': p_value}, ignore_index=True)
    
    return means, std_devs, axes, anova_results
import pandas as pd
import matplotlib.pyplot as plt
def task_func(data_dict):
    """
    Generates histograms for each column in the given DataFrame and checks if the value distributions are uniform.
    It prints a message for each non-uniform distribution.
    
    Parameters:
    - data_dict: A dictionary where keys are column names and values are lists of data points.
    
    Returns:
    - List[plt.Axes]: A list of matplotlib Axes objects, each representing the histogram for a column.
    """
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data_dict)
    
    # List to hold the Axes objects
    axes_list = []
    
    # Iterate over each column in the DataFrame
    for column in df.columns:
        # Create a histogram for the current column
        ax = df[column].hist(bins=20, alpha=0.7, figsize=(8, 6))
        axes_list.append(ax)
        
        # Check if the distribution is uniform
        if not is_uniform(df[column]):
            print(f"Non-uniform distribution detected in column: {column}")
    
    return axes_list
def is_uniform(series):
    """
    Checks if the distribution of a series is uniform.
    
    Parameters:
    - series: A pandas Series object.
    
    Returns:
    - bool: True if the distribution is uniform, False otherwise.
    """
    # Calculate the value counts
    value_counts = series.value_counts()
    
    # Check if all counts are equal
    return value_counts.nunique() == 1
data_dict = {
    'A': [1, 2, 2, 3, 3, 3],
    'B': [4, 4, 4, 4, 4, 4],
    'C': [5, 5, 6, 6, 7, 7]
}
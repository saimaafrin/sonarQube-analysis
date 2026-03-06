
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Constants
FEATURE_NAMES = ["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5"]

def task_func(data_matrix):
    # Standardize the data matrix
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data_matrix)
    
    # Create a DataFrame from the standardized data
    df_standardized = pd.DataFrame(standardized_data, columns=FEATURE_NAMES)
    
    # Calculate the mean of each row
    row_means = df_standardized.mean(axis=1)
    
    # Add the mean values to the DataFrame
    df_result = df_standardized.copy()
    df_result['Mean'] = row_means
    
    # Plot the distribution of the mean values
    fig, ax = plt.subplots()
    ax.hist(row_means, bins=10, edgecolor='black')
    ax.set_title('Distribution of Means')
    
    return df_result, ax
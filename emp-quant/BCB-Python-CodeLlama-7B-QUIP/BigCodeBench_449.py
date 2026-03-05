
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def task_func(data: pd.DataFrame) -> (pd.DataFrame, list):
    # Standardize the data using the StandardScaler
    scaler = StandardScaler()
    standardized_data = scaler.fit(data)

    # Create a list to store the histogram axes
    axes_list = []

    # Loop through each feature and draw a histogram
    for col in standardized_data.columns:
        # Get the histogram for this feature
        hist, bins = plt.hist(standardized_data[col], bins=20)

        # Create an axis for this histogram
        ax = plt.gca()
        ax.set_xlabel(f"Feature {col}")
        ax.set_ylabel("Count")
        ax.set_title(f"Histogram of Feature {col}")

        # Add the histogram to the list
        axes_list.append(ax)

    # Return the standardized data and the list of axes
    return standardized_data, axes_list
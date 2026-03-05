
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def task_func(data: pd.DataFrame) -> (pd.DataFrame, list):
    # Standardize the data using StandardScaler
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data)

    # Create a list to store the histogram axes
    axes_list = []

    # Draw a histogram for each feature with 20 bins
    for feature in standardized_data.columns:
        ax = plt.hist(standardized_data[feature], bins=20)
        axes_list.append(ax)

    return standardized_data, axes_list
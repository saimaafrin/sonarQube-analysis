import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def task_func(data: pd.DataFrame) -> (pd.DataFrame, list):
    # Standardize the data
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data)

    # Create a list of histogram axes
    axes_list = []

    # Draw a histogram for each feature
    for feature in standardized_data.columns:
        ax = plt.subplot(111)
        ax.hist(standardized_data[feature], bins=20)
        axes_list.append(ax)

    return standardized_data, axes_list
data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def task_func(data: pd.DataFrame) -> (pd.DataFrame, list):
    # Standardize the data using StandardScaler
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data)

    # Create a list to store the histogram axes
    axes_list = []

    # Draw a histogram for each feature
    for feature in standardized_data.columns:
        # Create a histogram for the current feature
        ax = plt.hist(standardized_data[feature], bins=20)
        axes_list.append(ax)

    return standardized_data, axes_list

# Plot the histograms
for ax in axes_list:
    ax.set_title(ax.get_title() + ' (Standardized)')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of ' + ax.get_title())
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_axis_off()

plt.show()
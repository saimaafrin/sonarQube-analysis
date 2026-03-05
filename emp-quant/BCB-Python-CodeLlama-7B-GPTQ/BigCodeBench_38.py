import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
FEATURE_NAMES = ["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5"]
def task_func(data_matrix):
    # Standardize the data
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data_matrix)

    # Calculate the mean of each row
    mean_values = standardized_data.mean(axis=1)

    # Create a DataFrame with the standardized data and the mean values
    df = pd.DataFrame(standardized_data, columns=FEATURE_NAMES)
    df['Mean'] = mean_values

    # Plot the histogram of the mean values
    fig, ax = plt.subplots()
    ax.hist(df['Mean'], bins=20)
    ax.set_title('Distribution of Means')
    ax.set_xlabel('Mean')
    ax.set_ylabel('Frequency')

    return df, ax
data_matrix = pd.DataFrame(
    [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20],
     [21, 22, 23, 24, 25]],
    columns=FEATURE_NAMES
)
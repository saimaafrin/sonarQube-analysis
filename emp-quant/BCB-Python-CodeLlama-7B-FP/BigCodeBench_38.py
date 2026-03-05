import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
FEATURE_NAMES = ["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5"]
def task_func(data_matrix):
    # Standardize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data_matrix)

    # Calculate the mean of each row
    mean_values = scaled_data.mean(axis=1)

    # Create a DataFrame with the standardized data and the mean of each row
    df = pd.DataFrame(scaled_data, columns=FEATURE_NAMES)
    df['Mean'] = mean_values

    # Visualize the distribution of the mean values with an histogram
    fig, ax = plt.subplots()
    ax.hist(df['Mean'], bins=50)
    ax.set_title('Distribution of Means')
    ax.set_xlabel('Mean')
    ax.set_ylabel('Frequency')
    plt.show()

    return df, ax
data_matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Check if DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")

    # Get list of numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    # Check if any numeric columns are present
    if not numeric_cols:
        raise ValueError("No numeric columns present in DataFrame")

    # Create a StandardScaler object
    scaler = StandardScaler()

    # Fit the scaler to the numeric columns
    scaler.fit(df[numeric_cols])

    # Transform the data using the scaler
    scaled_data = scaler.transform(df[numeric_cols])

    # Create a new DataFrame with the standardized data
    standardized_df = pd.DataFrame(scaled_data, columns=numeric_cols, index=df.index)

    # Plot the correlation matrix
    sns.heatmap(standardized_df.corr(), annot=True, cmap="coolwarm")

    # Return the standardized DataFrame and the figure object
    return standardized_df, plt.gcf()
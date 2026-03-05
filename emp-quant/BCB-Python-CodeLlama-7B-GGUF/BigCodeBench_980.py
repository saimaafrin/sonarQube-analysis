
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Check if DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")

    # Get numeric columns
    numeric_cols = df.select_dtypes(include=np.number).columns

    # Check if any numeric columns are present
    if not numeric_cols:
        raise ValueError("No numeric columns present")

    # Create correlation matrix
    corr_matrix = df[numeric_cols].corr()

    # Plot correlation matrix
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")

    # Standardize numeric columns
    scaler = StandardScaler()
    scaled_df = scaler.fit_transform(df[numeric_cols])

    # Return standardized DataFrame and figure object
    return scaled_df, fig
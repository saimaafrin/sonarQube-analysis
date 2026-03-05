
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def task_func(df, features):
    # Initialize the StandardScaler
    scaler = StandardScaler()

    # Fit the scaler to the features
    scaler.fit(features)

    # Transform the features
    transformed_features = scaler.transform(features)

    # Create a new DataFrame with the transformed features
    new_df = pd.DataFrame(transformed_features, columns=features.columns)

    return new_df
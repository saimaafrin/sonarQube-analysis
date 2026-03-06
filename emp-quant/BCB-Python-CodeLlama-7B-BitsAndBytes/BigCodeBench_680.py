
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def task_func(df, features):
    # Create a StandardScaler object
    scaler = StandardScaler()

    # Fit the scaler to the features
    scaler.fit(df[features])

    # Apply the scaler to the features
    scaled_features = scaler.transform(df[features])

    # Create a new DataFrame with the standardized features
    standardized_df = pd.DataFrame(scaled_features, columns=features)

    # Return the standardized DataFrame
    return standardized_df

# Standardize the features
standardized_df = task_func(df, features)

# Print the standardized DataFrame
print(standardized_df)
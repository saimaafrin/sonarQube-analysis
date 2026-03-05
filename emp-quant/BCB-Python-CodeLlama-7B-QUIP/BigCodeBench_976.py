
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(records: np.ndarray, random_seed: int = 0) -> pd.DataFrame:
    # Check if the input is a 2D array
    if records.ndim != 2:
        raise ValueError("The input must be a 2D array")

    # Shuffle the features
    shuffled_features = np.random.RandomState(random_seed).shuffle(records)

    # Normalize the values
    scaler = StandardScaler()
    normalized_features = scaler.fit_transform(shuffled_features)

    # Create a DataFrame with shuffled feature names
    feature_names = ["f" + str(i + 1) for i in range(normalized_features.shape[1])]
    return pd.DataFrame(normalized_features, columns=feature_names)
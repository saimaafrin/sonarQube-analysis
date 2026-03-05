import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(records: np.ndarray, random_seed: int = 0) -> pd.DataFrame:
    """
    Randomly shuffle the given array's features, normalize its values, then convert to a DataFrame with shuffled feature names.
    Notes:
        - This function normalizes data by subtracting the mean and scaling to unit variance.
        - Feature names are of format f{n}; for example, if the records have 5 features, feature names will be ["f1", "f2", "f3", "f4", "f5"] shuffled.
        - The function should raise the exception for: ValueError: If records is not 2D.
        - The function should output with:
            - pd.DataFrame: A pandas DataFrame containing the preprocessed data, with shuffled feature names.
    """
    # Check if records is 2D
    if records.ndim != 2:
        raise ValueError("Records must be 2D")

    # Shuffle the feature names
    feature_names = ["f" + str(i) for i in range(1, records.shape[1] + 1)]
    np.random.seed(random_seed)
    np.random.shuffle(feature_names)

    # Normalize the data
    scaler = StandardScaler()
    records_scaled = scaler.fit_transform(records)

    # Create a DataFrame with shuffled feature names
    df = pd.DataFrame(records_scaled, columns=feature_names)

    return df
records = np.random.rand(10, 5)
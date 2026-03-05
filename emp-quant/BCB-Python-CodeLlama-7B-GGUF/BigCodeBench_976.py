
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(records: np.ndarray, random_seed: int = 0) -> pd.DataFrame:
    """
    Randomly shuffle the given array's features, normalize its values, then convert to a DataFrame with shuffled feature names.

    Parameters:
    records (np.ndarray): The input array to preprocess.
    random_seed (int, optional): The random seed to use for shuffling. Defaults to 0.

    Returns:
    pd.DataFrame: A pandas DataFrame containing the preprocessed data, with shuffled feature names.

    Raises:
    ValueError: If records is not 2D.
    """
    if records.ndim != 2:
        raise ValueError("Records must be 2D")

    # Shuffle the feature names
    feature_names = [f"f{i+1}" for i in range(records.shape[1])]
    np.random.seed(random_seed)
    np.random.shuffle(feature_names)

    # Normalize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(records)

    # Create the DataFrame
    df = pd.DataFrame(scaled_data, columns=feature_names)

    return df
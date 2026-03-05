import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(records: np.ndarray, random_seed: int = 0) -> pd.DataFrame:
    """
    Shuffles the features of the given 2D array, normalizes its values, and converts to a DataFrame with shuffled feature names.
    
    Parameters:
    - records: A 2D numpy array of records.
    - random_seed: An integer to set the random seed for reproducibility.
    
    Returns:
    - A pandas DataFrame containing the preprocessed data with shuffled feature names.
    
    Raises:
    - ValueError: If records is not 2D.
    """
    if records.ndim != 2:
        raise ValueError("Input records must be a 2D array.")
    
    np.random.seed(random_seed)
    num_features = records.shape[1]
    feature_names = [f"f{i+1}" for i in range(num_features)]
    np.random.shuffle(feature_names)
    
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(records)
    
    df = pd.DataFrame(normalized_data, columns=feature_names)
    return df
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(records: np.ndarray, random_seed: int = 0) -> pd.DataFrame:
    """
    Shuffles the features of the given 2D array, normalizes its values, and converts to a DataFrame with shuffled feature names.
    
    Parameters:
    - records (np.ndarray): A 2D numpy array of records.
    - random_seed (int): The seed for the random number generator to ensure reproducibility.
    
    Returns:
    - pd.DataFrame: A pandas DataFrame containing the preprocessed data with shuffled feature names.
    
    Raises:
    - ValueError: If records is not 2D.
    """
    # Check if the input is 2D
    if records.ndim != 2:
        raise ValueError("Input records must be a 2D array.")
    
    # Shuffle the features
    np.random.seed(random_seed)
    shuffled_indices = np.random.permutation(records.shape[1])
    shuffled_records = records[:, shuffled_indices]
    
    # Normalize the values
    scaler = StandardScaler()
    normalized_records = scaler.fit_transform(shuffled_records)
    
    # Create DataFrame with shuffled feature names
    feature_names = [f"f{i+1}" for i in range(normalized_records.shape[1])]
    df = pd.DataFrame(normalized_records, columns=feature_names)
    
    return df
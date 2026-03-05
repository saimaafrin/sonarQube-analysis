import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(records: np.ndarray, random_seed: int = 0) -> pd.DataFrame:
    """
    Shuffles the features of the given 2D array, normalizes its values, and converts to a DataFrame with shuffled feature names.
    
    Parameters:
    records (np.ndarray): A 2D numpy array containing the records to be preprocessed.
    random_seed (int): The seed for the random number generator to ensure reproducibility.
    
    Returns:
    pd.DataFrame: A pandas DataFrame containing the preprocessed data, with shuffled feature names.
    
    Raises:
    ValueError: If records is not 2D.
    """
    if records.ndim != 2:
        raise ValueError("Input records must be a 2D numpy array.")
    
    np.random.seed(random_seed)
    feature_names = [f"f{i+1}" for i in range(records.shape[1])]
    np.random.shuffle(feature_names)
    
    scaler = StandardScaler()
    normalized_records = scaler.fit_transform(records)
    
    return pd.DataFrame(normalized_records, columns=feature_names)
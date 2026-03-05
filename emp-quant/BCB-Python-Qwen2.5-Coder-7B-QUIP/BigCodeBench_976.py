
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(records: np.ndarray, random_seed: int = 0) -> pd.DataFrame:
    if records.ndim != 2:
        raise ValueError("Input records must be 2D.")
    
    # Shuffle the feature names
    num_features = records.shape[1]
    feature_names = [f"f{i}" for i in range(1, num_features + 1)]
    np.random.shuffle(feature_names)
    
    # Normalize the records
    scaler = StandardScaler()
    normalized_records = scaler.fit_transform(records)
    
    # Create a DataFrame with shuffled feature names
    shuffled_df = pd.DataFrame(normalized_records, columns=feature_names)
    
    return shuffled_df
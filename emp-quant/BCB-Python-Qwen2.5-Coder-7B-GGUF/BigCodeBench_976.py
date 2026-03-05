
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(records: np.ndarray, random_seed: int = 0) -> pd.DataFrame:
    if records.ndim != 2:
        raise ValueError("Input records must be 2D")
    
    np.random.seed(random_seed)
    shuffled_indices = np.random.permutation(records.shape[1])
    shuffled_records = records[:, shuffled_indices]
    
    scaler = StandardScaler()
    normalized_records = scaler.fit_transform(shuffled_records)
    
    feature_names = [f"f{i+1}" for i in range(normalized_records.shape[1])]
    df = pd.DataFrame(normalized_records, columns=feature_names)
    
    return df
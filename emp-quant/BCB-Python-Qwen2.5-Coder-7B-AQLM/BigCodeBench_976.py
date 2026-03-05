
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(records: np.ndarray, random_seed: int = 0) -> pd.DataFrame:
    if records.ndim != 2:
        raise ValueError("Input records must be 2D")
    
    np.random.seed(random_seed)
    feature_names = [f"f{i+1}" for i in range(records.shape[1])]
    np.random.shuffle(feature_names)
    
    scaler = StandardScaler()
    scaled_records = scaler.fit_transform(records)
    
    df = pd.DataFrame(scaled_records, columns=feature_names)
    return df
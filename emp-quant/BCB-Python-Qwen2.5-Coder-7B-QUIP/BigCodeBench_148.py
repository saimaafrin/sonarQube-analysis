
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    # Create a copy of the DataFrame to avoid modifying the original
    df_encoded = df.copy()
    
    # Initialize the LabelEncoder
    encoder = LabelEncoder()
    
    # Fit and transform the specified column
    df_encoded[column_name] = encoder.fit_transform(df[column_name])
    
    return df_encoded
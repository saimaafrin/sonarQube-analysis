
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(df, dct, columns=None):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame.")
    
    if columns is None:
        columns = df.columns
    
    for col in columns:
        if col in dct:
            if df[col].dtype == 'object':
                encoder = LabelEncoder()
                df[col] = encoder.fit_transform(df[col])
            else:
                df[col] = (df[col] - df[col].mean()) / df[col].std()
    
    return df
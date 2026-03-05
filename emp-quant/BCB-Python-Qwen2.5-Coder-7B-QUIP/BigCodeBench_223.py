
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(df, dct, columns=None):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame.")
    
    if columns is None:
        columns = df.columns
    
    le = LabelEncoder()
    for col in columns:
        if df[col].dtype == 'category':
            df[col] = le.fit_transform(df[col])
    
    for col in columns:
        if df[col].dtype in ['int64', 'float64']:
            df[col] = (df[col] - df[col].mean()) / df[col].std()
    
    return df

import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the DataFrame
    df_standardized = scaler.fit_transform(df)
    
    # Convert the numpy array back to a DataFrame
    df_standardized = pd.DataFrame(df_standardized, columns=df.columns)
    
    return df_standardized
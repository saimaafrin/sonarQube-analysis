
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.exceptions import NotFittedException

def task_func(file_name: str) -> pd.DataFrame:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_name)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Identify numeric columns
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    
    if not numeric_columns:
        raise ValueError("Input does not have numeric columns.")
    
    # Apply MinMaxScaler to numeric columns
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
    
    return df
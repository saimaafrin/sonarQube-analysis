import pandas as pd
from sklearn.preprocessing import MinMaxScaler
def task_func(file_name: str) -> pd.DataFrame:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_name)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Identify numeric columns
    numeric_cols = df.select_dtypes(include=[int, float]).columns
    
    # Check if there are any numeric columns
    if not numeric_cols.empty:
        # Apply MinMaxScaler to numeric columns
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    else:
        raise ValueError("Input does not have numeric columns.")
    
    return df

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(file_name: str) -> pd.DataFrame:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_name)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Identify numeric columns
    numeric_columns = df.select_dtypes(include=['number']).columns
    
    # Check if there are any numeric columns
    if not numeric_columns.empty:
        # Apply MinMaxScaler to the numeric columns
        df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
    else:
        raise ValueError("Input does not have numeric columns.")
    
    # Return the DataFrame with normalized data
    return df
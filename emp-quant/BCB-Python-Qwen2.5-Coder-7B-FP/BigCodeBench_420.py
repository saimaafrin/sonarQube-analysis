import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(data):
    """
    Scales numeric columns of a data dictionary using the StandardScaler.
    
    Parameters:
    - data (pd.DataFrame): The input dataframe to scale.
    
    Returns:
    - pd.DataFrame: Dataframe with scaled numeric columns.
    """
    scaler = StandardScaler()
    numeric_cols = data.select_dtypes(include=[float, int]).columns
    scaled_data = data.copy()
    
    for col in numeric_cols:
        try:
            # Attempt to convert the column to float
            scaled_data[col] = scaled_data[col].astype(float)
            # Scale the column
            scaled_data[col] = scaler.fit_transform(scaled_data[col].values.reshape(-1, 1))
        except ValueError:
            # If conversion fails, leave the column unchanged
            pass
    
    return scaled_data
data = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [1.1, 2.2, 3.3, 4.4, 5.5],
    'C': ['a', 'b', 'c', 'd', 'e'],
    'D': [1, '2', 3, '4', 5]
})
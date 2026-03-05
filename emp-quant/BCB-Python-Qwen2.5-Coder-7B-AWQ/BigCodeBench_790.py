import heapq
from sklearn.preprocessing import StandardScaler
import pandas as pd
def task_func(df, col1, col2, N=10):
    # Check if the specified columns are in the DataFrame
    if col1 not in df.columns or col2 not in df.columns:
        raise ValueError(f"Columns {col1} and {col2} must be in the DataFrame.")
    
    # Standardize the specified columns
    scaler = StandardScaler()
    df['col1_scaled'] = scaler.fit_transform(df[[col1]])
    df['col2_scaled'] = scaler.fit_transform(df[[col2]])
    
    # Calculate the absolute differences between the standardized columns
    df['diff'] = abs(df['col1_scaled'] - df['col2_scaled'])
    
    # Get the indices of the N largest differences
    indices = df.nlargest(N, 'diff').index.tolist()
    
    return indices
df = pd.DataFrame({
    'a': [1, 2, 3, 4],
    'b': [1, 2, 3, 5]
})
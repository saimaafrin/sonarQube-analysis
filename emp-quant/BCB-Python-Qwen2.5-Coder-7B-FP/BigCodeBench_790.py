import heapq
from sklearn.preprocessing import StandardScaler
import pandas as pd
def task_func(df, col1, col2, N=10):
    # Check if the specified columns are in the DataFrame
    if col1 not in df.columns or col2 not in df.columns:
        raise ValueError(f"Columns {col1} and {col2} must be in the provided DataFrame.")
    
    # Standardize the specified columns
    scaler = StandardScaler()
    df[[col1, col2]] = scaler.fit_transform(df[[col1, col2]])
    
    # Calculate the differences between the standardized columns
    differences = abs(df[col1] - df[col2])
    
    # Find the indices of the N largest differences
    indices = heapq.nlargest(N, range(len(differences)), differences.get)
    
    return indices
df = pd.DataFrame({
    'a': [1, 2, 3, 4],
    'b': [1, 2, 3, 5]
})
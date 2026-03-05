import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(df, age, weight):
    """
    Filters and standardizes a given DataFrame based on specified age and weight criteria.
    
    Parameters:
    - df (pd.DataFrame): Input DataFrame containing at least 'Age' and 'Weight' columns.
    - age (int): Age threshold for filtering.
    - weight (int): Weight threshold for filtering.
    
    Returns:
    - pd.DataFrame: A DataFrame containing the filtered and standardized data.
    """
    # Check if required columns are present
    required_columns = ['Age', 'Weight']
    if not all(column in df.columns for column in required_columns):
        raise KeyError("Input DataFrame must contain 'Age' and 'Weight' columns.")
    
    # Filter the DataFrame based on age and weight criteria
    filtered_df = df[(df['Age'] < age) & (df['Weight'] > weight)]
    
    # Standardize the numerical values in the filtered DataFrame
    scaler = StandardScaler()
    standardized_df = pd.DataFrame(scaler.fit_transform(filtered_df), columns=filtered_df.columns)
    
    return standardized_df
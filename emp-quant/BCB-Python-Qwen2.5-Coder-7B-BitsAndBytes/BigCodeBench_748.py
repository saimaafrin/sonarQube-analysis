
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(df, age, weight):
    # Check if the required columns exist in the DataFrame
    required_columns = ['Age', 'Weight']
    if not all(column in df.columns for column in required_columns):
        raise KeyError("Input DataFrame must contain the required columns 'Age' and 'Weight'")
    
    # Filter the DataFrame based on the specified age and weight criteria
    filtered_df = df[(df['Age'] < age) & (df['Weight'] > weight)]
    
    # Standardize the numerical values in the filtered DataFrame
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(filtered_df[['Age', 'Weight']])
    
    # Create a new DataFrame with the scaled data and original non-standardized columns
    result_df = filtered_df.copy()
    result_df[['Age', 'Weight']] = scaled_data
    
    return result_df
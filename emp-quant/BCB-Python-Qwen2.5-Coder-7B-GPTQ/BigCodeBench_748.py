import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(df, age, weight):
    # Check if required columns are present
    required_columns = ['Age', 'Weight']
    if not all(column in df.columns for column in required_columns):
        raise KeyError("Input DataFrame must contain 'Age' and 'Weight' columns.")
    
    # Filter the DataFrame based on the given criteria
    filtered_df = df[(df['Age'] < age) & (df['Weight'] > weight)]
    
    # Standardize the filtered DataFrame
    scaler = StandardScaler()
    standardized_df = pd.DataFrame(scaler.fit_transform(filtered_df[['Age', 'Weight']]), columns=['Age', 'Weight'])
    
    # Reconstruct the DataFrame with the standardized values and original non-standardized columns
    result_df = pd.concat([standardized_df, df.drop(columns=['Age', 'Weight'])], axis=1)
    
    return result_df
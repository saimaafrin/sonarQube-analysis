
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(df, age, weight):
    # Check if the required columns are present in the DataFrame
    if 'Age' not in df.columns or 'Weight' not in df.columns:
        raise KeyError("Input DataFrame must contain the columns 'Age' and 'Weight'.")

    # Filter the DataFrame based on the specified age and weight criteria
    filtered_df = df[(df['Age'] < age) & (df['Weight'] > weight)]

    # If the filtered DataFrame is empty, return an empty DataFrame
    if filtered_df.empty:
        return pd.DataFrame(columns=df.columns, dtype=float)

    # Initialize the StandardScaler
    scaler = StandardScaler()

    # Standardize the numerical values in the filtered DataFrame
    scaled_df = scaler.fit_transform(filtered_df)

    # Create a new DataFrame with the standardized values
    result_df = pd.DataFrame(scaled_df, columns=filtered_df.columns)

    return result_df
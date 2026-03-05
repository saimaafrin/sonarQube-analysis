
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(df, age, weight):
    # Check if the required columns are present in the input DataFrame
    if 'Age' not in df.columns or 'Weight' not in df.columns:
        raise KeyError("The input DataFrame does not contain the required columns 'Age' and 'Weight'.")

    # Filter the DataFrame based on the specified age and weight criteria
    filtered_df = df[(df['Age'] < age) & (df['Weight'] > weight)]

    # Standardize the numerical values in the filtered DataFrame
    scaler = StandardScaler()
    scaled_df = scaler.fit_transform(filtered_df)

    return scaled_df
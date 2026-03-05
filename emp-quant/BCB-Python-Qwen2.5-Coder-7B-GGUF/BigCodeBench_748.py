
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(df, age, weight):
    # Check if the required columns are present in the DataFrame
    required_columns = ['Age', 'Weight']
    if not all(column in df.columns for column in required_columns):
        raise KeyError("The input DataFrame must contain the required columns 'Age' and 'Weight'.")

    # Filter the DataFrame based on the specified age and weight criteria
    filtered_df = df[(df['Age'] < age) & (df['Weight'] > weight)]

    # Standardize the numerical values in the filtered DataFrame
    scaler = StandardScaler()
    standardized_df = pd.DataFrame(scaler.fit_transform(filtered_df[required_columns]), columns=required_columns)
    standardized_df = pd.concat([standardized_df, filtered_df.drop(columns=required_columns)], axis=1)

    return standardized_df